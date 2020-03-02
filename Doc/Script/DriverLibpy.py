from ExcelDriver import ExcelDriver
from Helper import Helper
import logging
from ObjRepoParser import ObjRepoParser
from TCParser import TCParser
from WebObject import WebObject
from Switch import Switch
import sys,os,traceback,inspect
from Mail import Mail 
from Action import Action 
from DBConnector import DBConnector
from TestConfig import TestConfig
from LoggerHandler import LoggerHandler
from Suite import Suite
from CommLineHandler import CommLineHandler
from StringParser import StringParser



LOG_FILENAME = Project.Path+"TestRepo\ExceptionLog\Log.txt"
AttachList = [LOG_FILENAME]
logging.basicConfig(filename=LOG_FILENAME, format='%(message)s',level=logging.INFO, filemode='w')
ErrDesc= ""


def main():
  TestConfig.IsIgnore = 'N'
  ObjSuite = Suite();
  ObjWebObject = WebObject();
  ObjAction = Action()
  ObjSwitch = Switch()
  ObjCommLineHandler = CommLineHandler();
  configDict = Helper.ReadConfig()
  ObjCommLineHandler.ProcessCommandLine()
  #SuitName = TestConfig.SuiteToRun
  SuitNameList = StringParser.splitStr(TestConfig.SuiteToRun,",") 
  #if(TestConfig.SuiteToRun is None or TestConfig.SuiteToRun == ""):
  if(SuitNameList[0] is None or str(SuitNameList[0]) == ""):
    SuitNameList = StringParser.splitStr(Helper.ReadConfig().get("SuitName"),",");
    #TestConfig.SuiteToRun = SuitName
  for SuitName in SuitNameList:
    #Clear Out the temp directory
    from FileIO import FileIO
    FileIO.emptyDir(TestConfig.TempLocation)
    TestConfig.SuiteToRun = SuitName
    LoggerHandler.InsertAutomationExecution();
    OrName = ObjSuite.GetObjectRepositoryName(SuitName);
    TestConfig.ObjRepName = OrName
    ExcelPath = ObjSuite.GetFilePath(SuitName)
    if StringParser.TextContains("^DDT",SuitName):
      TestConfig.SuiteType = "DDT"
      TCSheetName = "TestStep"
      TestDataSheet = "TestData"
      #OrName = "ObjRep"
    else:
      TestConfig.SuiteType = "REG"
      TCSheetName = SuitName
      TestDataSheet = ""
    StartTime = Helper.GetCurrentTime();
    myExcelVar = ExcelDriver(ExcelPath)
    TCRecords = myExcelVar.loadWorkSheetIntoMem(TCSheetName)  
    Log.Message("Test Case records:" + str(len(TCRecords)))
    if TestDataSheet != "":
      TDrecords = myExcelVar.loadWorkSheetIntoMem(TestDataSheet)
      Log.Message("Test Data records:" + str(len(TestDataSheet)))
    else:
      TDrecords = None
  
    ObjRecords = myExcelVar.loadWorkSheetIntoMem(OrName) 
    Log.Message("Objerepo records:" + str(len(ObjRecords)))
    ElapsedTime = Helper.GetTimeDiffInSecond(StartTime,Helper.GetCurrentTime())
    Log.Message("Time Taken To Read Object repository: " + str(ElapsedTime))
  
  
    xobj = ObjRepoParser(ObjRecords)
    objRepo = ObjRepoParser.getDict(ObjRecords)
    StartTime = Helper.GetCurrentTime();
    Log.Message("TCRecords list",str(TCRecords))
    MyTCParser = TCParser(TCRecords,TDrecords)
    if StringParser.TextContains("^DDT",SuitName):
      myInputData = MyTCParser.ddtInputTCParser()
    else:
      myInputData = MyTCParser.regInputTCParser()
    ElapsedTime = Helper.GetTimeDiffInSecond(StartTime,Helper.GetCurrentTime())
    Log.Message("Time Taken To Normalize Login data: " + str(ElapsedTime))
    #Srt Fun  
    
  
    for k,v in myInputData.items():
      #Set isIgnore to N when the new testcase is fetched from dictionary
      TestConfig.IsIgnore = 'N';
      if TestConfig.StopSuite == "Y":
        Log.Error("Stopping Dictionary Loop")
        myInputData = []
        Runner.Stop()
        raise Exception("Stopping For Loop Forcefully")
        break
      TestConfig.TestCaseId = k
      templist = myInputData[k]
      tcid = Log.CreateFolder(k)
      Log.PushLogFolder(tcid)
      #SumruList = Extrct Infor for Each TCs
      for item in templist:
        if TestConfig.StopSuite == "Y":
          Log.Message("Manual Stop Detected: flushing out current test case")
          templist = []
          #Runner.Stop()
          break
        TestConfig.TestCaseSteps			  =		 str(item[MyTCParser.tcHeader['TC_STEP']]);
        ActionType 					            =    str(item[MyTCParser.tcHeader['ACTION']]);
        ObjectAlias					            =		 str(item[MyTCParser.tcHeader['ObjectAlias']]);
        PropertyList 				            = 	 objRepo[str(item[MyTCParser.tcHeader['ObjectAlias']])];
        TestConfig.Parameter1 					= 	 str(item[MyTCParser.tcHeader['Param1']]);
        TestConfig.Parameter2 					= 	 str(item[MyTCParser.tcHeader['Param2']]);
        testDet = str(TestConfig.TestCaseSteps) + ";" + str(ActionType) + ";" + str(ObjectAlias) + ";" + str(PropertyList) + ";" + str(TestConfig.Parameter1) + ";" + str(TestConfig.Parameter2) + ";IsIgnore=" + str(TestConfig.IsIgnore)
        Log.Message("DEBUGBEF:"+TestConfig.TestCaseSteps,testDet, pmHighest, None , Sys.Desktop)
        if(ObjectAlias == "TCEND" and TestConfig.IsIgnore == 'Y'):
          TestConfig.IsIgnore = 'N';

        try:
          if(TestConfig.IsIgnore == 'N'):
            if(ObjectAlias == "" or ObjectAlias == " "):pass
            if(ObjectAlias == "TCBEGIN"):
              LoggerHandler.InsertAutomationExecutionSummary();
              #TestConfig.TestCaseName = StringParser.remAllSpecialCharacters(TestConfig.TestCaseSteps)
              TestConfig.TestCaseName = TestConfig.TestCaseSteps#StringParser.remAllSpecialCharacters(TestConfig.TestCaseSteps)
            if(ObjectAlias == "TCEND"): 
              LoggerHandler.UpdateAutomationExecutionSummary("Pass");
            Log.Message("DEBUGAFT:"+TestConfig.TestCaseSteps,testDet, pmHighest, None , Sys.Desktop)
            ObjSwitch.IMSOperation(ActionType,PropertyList,TestConfig.Parameter1 ,TestConfig.Parameter2);
            if(ObjectAlias == "TCBEGIN"):
              LoggerHandler.LogInfo("Info",TestCaseSteps=TestConfig.TestCaseName+" Start",CustomMessage="",Parameter1=TestConfig.Parameter1,Parameter2=TestConfig.Parameter2)
            elif(ObjectAlias == "TCEND"):
              LoggerHandler.LogInfo("Info",TestCaseSteps=TestConfig.TestCaseName+" End",CustomMessage="",Parameter1=TestConfig.Parameter1,Parameter2=TestConfig.Parameter2)
            else:
              if(ActionType !=  "REPORT"):
                LoggerHandler.LogInfo("Info",TestCaseSteps=TestConfig.TestCaseSteps,CustomMessage="",Parameter1=TestConfig.Parameter1,Parameter2=TestConfig.Parameter2)
        except Exception as e:
            TestConfig.IsIgnore = 'Y'
            LoggerHandler.UpdateAutomationExecutionSummary("Failed");#Completed with Errors
            exc_type, exc_value, exc_traceback = sys.exc_info()
            exc_info =(exc_type, exc_value, exc_traceback)
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            ErrDesc = '\n'.join('!! ' + line for line in lines) 
            ErrDesc2 = ''.join('!! ' + line for line in lines) 
            Log.Message(ErrDesc)
            ExcpMsg = str(aqString.Replace(aqString.Replace(aqString.Replace(aqString.Replace(ErrDesc2,"'",""),'"',""),"<","["),">","]"))
            LoggerHandler.LogInfo("Failed",TestCaseSteps=TestConfig.TestCaseSteps,CustomMessage=ExcpMsg,Parameter1=TestConfig.Parameter1,Parameter2=TestConfig.Parameter2)
            LoggerHandler.LogInfo("Info",TestCaseSteps=TestConfig.TestCaseName+" End",CustomMessage="",Parameter1="",Parameter2="")
            logging.error("",ErrDesc) 
            
            logging.info("Unexpected Exception: "
            +"\n Test Description : {"+TestConfig.TestCaseSteps+"}\n"
            +"\n Action : {"+ActionType+"}\n"
            +"\n Object Alias : {"+str(item[MyTCParser.tcHeader['ObjectAlias']])+"}\n"
            , exc_info=True)
          
            ObjAttributes = Log.CreateNewAttributes()
            ObjAttributes.Bold = True
            ObjAttributes.BackColor = clYellow
            ObjAttributes.FontColor = clRed
            Log.Error(traceback.format_exc(), traceback.format_exc(), pmNormal, ObjAttributes)
            Log.Message("StopSuite value in Except: " + TestConfig.StopSuite)
            if TestConfig.StopSuite == "Y":
              myInputData = []
              raise Exception("Stopping Suite Execution Forcefully")
            break
            #Helper.closeAllBrowser()
      Log.PopLogFolder()

    LoggerHandler.UpdateAutomationExecution("Completed")
    LoggerHandler.ExportTestResultIntoExcel();
    ObjList = list();
    ObjList.append(TestConfig.TRLocation)
  Mail.SendMail("ImsAutomation@seic.com","vroy1@seic.com,mxgupta@seic.com,IMSDWQATeam@seicx.com","IMS Automation Report | "+ SuitName+" | Run By: "+Helper.GetLoginUser()+" | Run ID: "+str(TestConfig.Execution_Id),"http://imsautomation1/ReportPage.aspx",Attachments=ObjList);