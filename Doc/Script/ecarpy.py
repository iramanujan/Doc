from Helper import Helper
#from Action import Action
from WebObject import WebObject
from FileIO  import FileIO
from TestConfig import TestConfig
from StringParser import StringParser
from LoggerHandler import LoggerHandler

class ECR:
	REPQUEID = ""
  
	def __init__(self):
		Log.Message("Initializing ECR Class");

	def getECRQueID(QueuIDObj):
		ECR.REPQUEID = StringParser.remAllWhiteSpaces(QueuIDObj.textContent)# removeStrSpace(QueuIDObj.textContent)
		Log.Message("QueID: " + ECR.REPQUEID)
  
	def waitTillReqComp(TimeOutInMin=Helper.ReadConfig().get("timeout")):
	  from PlatFormAdmin import PlatFormAdmin
	  ServerName = Helper.ReadConfig().get("NetikSrvName")
	  DatabaseName = Helper.ReadConfig().get("NetikDbName")
	  SQLCommand = "select BatchStatusId from netikext.ecr.ReportQueueHistory where ReportQueueId = '" + ECR.REPQUEID +"'"
	  result = -1
	  StartTime = Helper.GetCurrentTime()
	  ElapsedTime = 0
	  while result != 3 or result != 6:
	    if(ElapsedTime == 3):
	      Log.Message("It's been 3 minutes waiting for job to finish, Please check app stat")
	    if(int(ElapsedTime) > int(TimeOutInMin)):
	      LoggerHandler.LogInfo("Failed",CustomMessage="Job request for Report Queue not Finished",Parameter1="Report Queue: " + ECR.REPQUEID)
	      return None
	    OjDBConnector = DBConnector()
	    dbResult = OjDBConnector.GetDBValue(SQLCommand,ServerName,DatabaseName,None,None)
	    result = dbResult[0][0]
	    if result==3:
	      LoggerHandler.LogInfo("Info",CustomMessage="Validate Status From Database",Parameter1="Batch ID:  "+ ECR.REPQUEID,Parameter2="Status: Complete")
	    elif result ==6:
	      LoggerHandler.LogInfo("Info",CustomMessage="Validate Status From Database",Parameter1="Batch ID:  "+ ECR.REPQUEID,Parameter2="Status: Incomplete")
	    else:
	      LoggerHandler.LogInfo("Info",CustomMessage="Validate Status From Database",Parameter1="Batch ID:  "+ ECR.REPQUEID,Parameter2="Status: Fail")
	    SQLCommand2 = "select SubmittedBy from netikext.ecr.ReportQueueHistory where ReportQueueId = '" + ECRLib.REPQUEID +"'"
	    dbResult2 = OjDBConnector.GetDBValue(SQLCommand2,ServerName,DatabaseName,None,None)
	    PlatFormAdmin.USERID = ""
	    PlatFormAdmin.USERID = dbResult2[0][0]
	    Log.Message(PlatFormAdmin.USERID)
	    aqUtils.delay(1000,"Waiting for Job to Finish" + ECR.REPQUEID)
	    ElapsedTime = Helper.GetTimeDiffInMinutes(StartTime,Helper.GetCurrentTime());

	def SaveBatchId(Self,ParamList):
		ObjAction = Action();
		FileIO.createDir(TestConfig.TempLocation)
		FileLocation =  Project.Path+"\\"+Helper.ReadConfig().get("EcrBatchFileLocation")
		BatchID = ObjAction.GetText(ParamList);
		TcName = TestConfig.TestCaseId
		FileIO.WriteTextIntoFile(FileLocation,BatchID+":"+TcName)
		Log.Message("Batch-ID: " + BatchID)
   
	def ReadFileLineByLine(FileLocation):
		ObjWebObject = WebObject()
		from Action import Action
		ObjAction = Action()
		LoginUserId = Helper.GetLoginUser()
		LoginUserFolder = "D:\\"+str(LoginUserId)
		FileIO.createDir(LoginUserId)
		#FileLocation =  Project.Path+Helper.ReadConfig().get("EcrBatchFileLocation")
		with open(FileLocation) as f:
		  for line in f:
		    aqString.ListSeparator = ":"
		    batchId = aqString.GetListItem(line,0)
		    tcName = aqString.GetListItem(line,1)
        
		    Log.Message("Batch ID: "+batchId+"; TC Name: "+tcName)
        
		    aqUtils.Delay(1000)
		    ObjAction.KeyIn(WebObject.getPropertyList("SearchJobHistory"),batchId);
		    aqUtils.Delay(1000)    
		    ObjAction.Click(WebObject.getPropertyList("SearchBtn"));
		    aqUtils.Delay(1000)
		    #TestConfig.IsRenameFile = 1
		    TCLocation = ""
		    if(ECR.GetJobStatus(batchId)):
		      if(TestConfig.IsRenameFile == 1):
		        TCLocation = LoginUserFolder+"\\"+tcName
		        FileIO.createDir(TCLocation)
		      else:
		        TCLocation =  Project.Path+Helper.ReadConfig().get("tempFileLoc")+ "\\"+tcName
		    Log.Message(TCLocation)
		     #IMPORTANT : Add Instruction for Export File.
		    Action.ECRExportFile(TCLocation)
#		  if(IsRename == 1):
#		    ZipFileList = GetZipFileList(LoginUserFolder)
#     
#  def RenameFiles(ParentPath):
#    SubDirList = FileIO.GetAllSubFolderList(ParentPath)
#    for SubDir in SubDirList:
#      Log.Message("SubDir Path"+SubDir)
#      FileList = FileIO.GetAllSubFolderList(SubDir)
#      for File in FileList:  
#        Log.Message("File Path"+File)
#        FileName = FieldList.split(".")[0]
#        FileExt  = FieldList.split(".")[1]
#        if(FileExt == "xlsx" or FileExt == "xls"):
#          StringParser.Right( FileName FileExt
     
	def GetText(self,PropertyList):
	  from Action import Action
	  ObjAction = Action()
	  ObjWebObject = WebObject()
	  WebElement = ObjAction.GetObject(WebObject.getPropertyList(PropertyList))
	  LoggerHandler.LogInfo("Info",CustomMessage=WebElement.textContent)
 
	def PressEnter(self):
		aqUtils.delay(1000)
		Sys.OleObject("WScript.Shell").SendKeys("{ENTER}")
		Sys.Desktop.Keys("[ENTER]");
		aqUtils.delay(1000)
 
	def GetJobStatus(args):
		try:
		  from Action import Action
		  ObjAction = Action()
		  ObjWebObject = WebObject()
		  FirstRcd = ObjAction.GetObject(WebObject.getPropertyList("FirstRcd2"))
		  if(FirstRcd is None):
		    NewMessage = ObjAction.GetObject(WebObject.getPropertyList("NewMessage"))
		    if(NewMessage is None):
		      LoggerHandler.LogInfo("Failed",CustomMessage="No Record Found.",Parameter1=args)
		    else:
		      LoggerHandler.LogInfo("Failed",CustomMessage=MyEle4.textContent,Parameter1=args)
		  else:
		    NewBatchId = ObjAction.GetObject(WebObject.getPropertyList("NewBatchId"))
		    NewRequestDescription = ObjAction.GetObject(WebObject.getPropertyList("NewRequestDescription"))
		    NewJobStatus = ObjAction.GetObject(WebObject.getPropertyList("NewJobStatus"))
		    Test_Status = "Batch ID:  "+ (NewBatchId.textContent)+"    Request Description  " + (NewRequestDescription.textContent)+"STATUS=  "+(NewJobStatus.textContent)+"   "
		    if(NewJobStatus.textContent == "Completed"):
		      LoggerHandler.LogInfo("Pass",CustomMessage=Test_Status)
		    else:
		      LoggerHandler.LogInfo("Failed",CustomMessage=Test_Status)
		  return True;        
		except Exception as e:
		  LoggerHandler.LogInfo("Failed",CustomMessage=str(e))
		  return False;  
       
	def ListItem(self,PropertyList,VisibleText):
		WebElement = WebObjectHandler.FindWebObject(PropertyList);
		WebElement.scrollIntoView(True)
		WebElement.Click()
		Sys.Desktop.Keys(aqConvert.VarToStr(VisibleText));
		aqUtils.Delay(1000);
		Sys.Desktop.Keys("[Tab]");
		aqUtils.Delay(1000);
		
