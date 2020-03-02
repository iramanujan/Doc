from StringParser import StringParser
from Helper import Helper
from ECR import ECR
from DBConnector import DBConnector
from WebObjectHandler import WebObjectHandler
from WebObject import WebObject
import Action
from LoggerHandler import LoggerHandler
from MDB import MDB
from FileIO  import FileIO
from TestConfig import TestConfig

class PlatFormAdmin:
	GenevaRequestTime = "";
	USERID = "";
  
	def __init__(self):
		Log.Message("Initializing PlatFormAdmin Class");
		
	def SetGenevaRequestTime(self,PropertyList):
	  aqUtils.Delay(10000,"Waiting for Enable Submit Button...")
	  ObjAction = Action.Action()
	  ObjAction.Click(PropertyList);
	  PlatFormAdmin.GenevaRequestTime = Helper.GetFCurrTimeHMS()
	  
	def GetSubmittedBy():
	  ServerName = Helper.ReadConfig().get("NetikSrvName")
	  DatabaseName = Helper.ReadConfig().get("NetikDbName")
	  RequestId = aqString.Trim(TestConfig.GetValeFromTempDict("GETQUEUEID"),aqString.stAll)
	  SQLCommand = "select SubmittedBy from netikext.ecr.ReportQueueHistory where ReportQueueId = '" + str(RequestId) +"'"
	  OjDBConnector = DBConnector()
	  dbResult = OjDBConnector.GetDBValue(SQLCommand,ServerName,DatabaseName,None,None)
	  PlatFormAdmin.USERID = str(dbResult[0][0])
	  Log.Message("PlatFormAdmin: " + PlatFormAdmin.USERID)
	  
	def VerGenevaReqDetails(AppDetStr,ExcelDetStr):
	  result = False
	  LoggerHandler.LogInfo("Info",CustomMessage="Excel RSL String",Parameter1=ExcelDetStr)
	  LoggerHandler.LogInfo("Info",CustomMessage="Application RSL String",Parameter1=AppDetStr)
	  #Remove timestamp numbers at the end of the string
	  AppDetVal = StringParser.regexReplace('_\d+\.',AppDetStr,'_.')
	  InputStr = StringParser.remAllWhiteSpaces(ExcelDetStr)
	  AppDetVal = StringParser.remAllWhiteSpaces(AppDetVal)
	  if TestConfig.TestCaseName == "Geneva_Request_Calendars":
	    AppDetVal = StringParser.regexReplace('[\d]{2}/[\d]{2}/[\d]{4}',AppDetVal,'')
	  #Replace USER-ID By Blank Space.
	  PlatFormAdmin.GetSubmittedBy()
	  AppDetVal = StringParser.replace(AppDetVal,PlatFormAdmin.USERID,"")
	  LoggerHandler.LogInfo("Info",CustomMessage="RSL String After Format",Parameter1=AppDetVal)
	  Log.Message("InputSTR and AppDetVal","InputSTR: " + InputStr + "AppDetVal: " + AppDetVal)
	  if InputStr == AppDetVal:
	    result = True
	  return result
	  
	def VerifyGenevaRSLString(self,objSelector,XlDetStr):  
	  result = False
	  act = Action.Action()
	  FrqReqRunType = WebObjectHandler.FindWebObject(WebObject.getPropertyList("GenevaRadBtnRunTypeFrequentRequest"))
	  SchdOvrCronRunType =  WebObjectHandler.FindWebObject(WebObject.getPropertyList("GenevaRadBtnScheduleOvernightCron"))
	  if FrqReqRunType.checked:
	    act.Sync(WebObject.getPropertyList("GenevaFreqReqStatFirstRecStatus"),5)
	    reqStartTime = act.GetText(WebObject.getPropertyList("GenevaFreqReqStatFirstRecStartTime"))
	    reqStartTime = StringParser.split(reqStartTime," ")[1]
	    timeDiff = Helper.GetTimeDiffInSecond(PlatFormAdmin.GenevaRequestTime,reqStartTime)
	    if timeDiff > 0:
	      act.Click(WebObject.getPropertyList("GenevaFreqReqStatFirstRecDetails"))
	      FreqReqDet = WebObjectHandler.FindWebObject(WebObject.getPropertyList("GenevaDetailContent"))
	      result = PlatFormAdmin.VerGenevaReqDetails(FreqReqDet.innerText,XlDetStr)
	  
	  if(SchdOvrCronRunType.checked):
	    SchdOvrCronDet = act.Sync(objSelector,5)
	    result = PlatFormAdmin.VerGenevaReqDetails(SchdOvrCronDet.innerText,XlDetStr)
	  
	  if(result):
	    LoggerHandler.LogInfo("Pass",TestCaseSteps="Validate RSL String",CustomMessage="Checking Raised Geneva Request Details",Parameter1=XlDetStr);
	  else:
	    LoggerHandler.LogInfo("Failed",TestCaseSteps="Validate RSL String",CustomMessage="Checking Raised Geneva Request Details",Parameter1=XlDetStr);
	
	def VarifyJobStatus(self):
	  ColumnName = "Batch ID"
	  RequestId = aqString.Trim(TestConfig.GetValeFromTempDict("GETQUEUEID"),aqString.stAll)
	  
	  ColumnPosition = MDB.GetColumnPosition(WebObject.getPropertyList("GenevaReqStatTableHeader"),ColumnName)
	  if ColumnPosition == 0:
	    return False;
	  
	  ObjAction = Action.Action()
	  WebElement = ObjAction.Sync(WebObject.getPropertyList("GenevaReqStatTableBody"),TimeOutInMin=Helper.ReadConfig().get("timeout"))
	  
	  if (WebElement is not None):
	    WebElementChildElementCount = WebElement.childElementCount
	    WebElementChildren = WebElement.children
	    for index in range ( 0 , WebElementChildElementCount):
	      GrandChildren = WebElementChildren.item(index).children
	      CellValue = str(GrandChildren.item(ColumnPosition - 1).textContent)
	      if(CellValue == RequestId):
	        RowPosition = str(index + 1)
	        break
	        
	    Log.Message("Rolumn Position = " + str(RowPosition) + " Job ID = " + str(RequestId))
	    StatusColVar = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("StatusColVar"),"ROWPOS",RowPosition)	    	    
	    Status = StringParser.RemoveSpaces(ObjAction.GetText(StatusColVar))
	    if Status == "Complete":
	      LoggerHandler.LogInfo("Pass",CustomMessage="Job Request Completed",Parameter1=Status)
	    else:
	      LoggerHandler.LogInfo("Failed",CustomMessage="Job Request Completed",Parameter1=Status)
	  return False;

	def SubmitInvestierRequest(self,TimeOutInMin=Helper.ReadConfig().get("timeout")):
	  Log.Message(str(Helper.ReadConfig().get("timeout")))
	  obj = None
	  InvestSubmitBtn = WebObjectHandler.FindWebObject(WebObject.getPropertyList("InvestierBtnSubmit"))
	  InvestSubmitBtn.scrollIntoView(True)
	  InvestSubmitBtn.click()
	  act = Action.Action()
	  OverlaySpinner = WebObject.getPropertyList("OverlaySpinner")
	  act.WaitTillSpinnerActive(OverlaySpinner,Helper.ReadConfig().get("timeout"))
	  obj = act.GetObject(WebObject.getPropertyList("AlertMsgRequestsubmittedSuccessfully"))
	  StartTime = Helper.GetCurrentTime()
	  ElapsedTime = 0;
	  while obj is None:
	    if(ElapsedTime == 3):
	      Log.Message("It's been 3 minutes finding this object, Please check app stat")
	    if(int(ElapsedTime) > int(TimeOutInMin)):
	      LoggerHandler.LogInfo("Failed",CustomMessage="Unable to Find Alert Message",Parameter1="Submitted Successfully")
	      return None
	    PageObj = TestComplete.ObjPage
	    PageObj.Wait(2000)
	    act.WaitTillSpinnerActive(WebObject.getPropertyList("OverlaySpinner"),Helper.ReadConfig().get("timeout"))
	    concObj = act.GetObject(WebObject.getPropertyList("AlertMsgMaxConcReqReached"))
	    if concObj is not None:
	      TestComplete.hardWait(60000,"Wait for max 10 concurrent jobs to finish")
	      WarnOkBtn = act.GetObject(WebObject.getPropertyList("BtnOkSuccess"))
	      WarnOkBtn.scrollIntoView(True)
	      WarnOkBtn.click()
	      TestComplete.hardWait(8000)
	      InvestSubmitBtn.scrollIntoView(True)
	      InvestSubmitBtn.click()
	    reqRunning = act.GetObject(WebObject.getPropertyList("AlertMsgReqAlreadyRunning"))
	    if reqRunning is not None:
	      TestComplete.hardWait(60000,"Request is already running for current client")#call aqUtils.Delay(60000,"Request is already running for current client")
	      WarnOkBtn = act.GetObject(WebObject.getPropertyList("BtnOkSuccess"))
	      WarnOkBtn.scrollIntoView(True)
	      WarnOkBtn.click()
	      TestComplete.hardWait(8000)
	      InvestSubmitBtn.scrollIntoView(True)
	      InvestSubmitBtn.click()
	    obj = act.GetObject(WebObject.getPropertyList("AlertMsgRequestsubmittedSuccessfully"))
	    TestComplete.hardWait(1000,"Waiting for Obj with Selector: AlertMsgRequestsubmittedSuccessfully")
	    ElapsedTime = Helper.GetTimeDiffInMinutes(StartTime,Helper.GetCurrentTime())
	  return obj
	  
	def WaitTillGenevaRequestComplete(self):
	  ServerName = Helper.ReadConfig().get("NetikSrvName")
	  DatabaseName = Helper.ReadConfig().get("NetikDbName")
	  RequestId = aqString.Trim(TestConfig.GetValeFromTempDict("GETQUEUEID"),aqString.stAll)
	  TimeOutInMin=Helper.ReadConfig().get("timeout")
	  SQLCommand = "select BatchStatusId from netikext.ecr.ReportQueueHistory where ReportQueueId = '" + str(RequestId) +"'"
	  result = 0
	  ElapsedTime = 0;
	  StartTime = Helper.GetCurrentTime()
	  aqUtils.Delay(10000,"Validating Job Status from Database...")
	  while result != 3 and result != 6:
	    if(ElapsedTime == 3):
	      Log.Message("It's been 3 minutes waiting for job to finish, Please check app stat")
	    if(int(ElapsedTime) > int(TimeOutInMin)):
	      LoggerHandler.LogInfo("Failed",CustomMessage="Job request for Report Queue not Finished",Parameter1="Report Queue: " + str(RequestId))
	      return None
	      
	    OjDBConnector = DBConnector()
	    dbResult = None;
	    aqUtils.Delay(5000,"Validating Job Status from Database...")
	    dbResult = OjDBConnector.GetDBValue(SQLCommand,ServerName,DatabaseName,None,None)
	    
	    if(dbResult):
	      result = dbResult[0][0]
	      Log.Message(str(result))
	    elif(len(dbResult) > 0):
	      result = dbResult[0][0]
	      Log.Message(str(result))
	    else:
	      result = 0
	  if(result == 3):
	    LoggerHandler.LogInfo("Pass",CustomMessage="Validate Status From Database",Parameter1="Batch ID:  "+ str(RequestId),Parameter2="Status: Complete")
	  elif(result == 6):
	    LoggerHandler.LogInfo("Pass",CustomMessage="Validate Status From Database",Parameter1="Batch ID:  "+ str(RequestId),Parameter2="Status: Incomplete")
	  else:
	    LoggerHandler.LogInfo("Failed",CustomMessage="Validate Status From Database",Parameter1="Batch ID:  "+ str(RequestId),Parameter2="Status: Fail")