from DBConnector import DBConnector
from Switch import Switch
from WebObject import WebObject
from WebObjectHandler import WebObjectHandler
from Mail import Mail
from TestComplete import TestComplete
from TCNameMapping import TCNameMapping
from Action import Action
from StringParser import StringParser
from Helper import Helper
from FileIO import FileIO
from ConfigReader import ConfigReader
from ExcelDriver import ExcelDriver
from ObjRepoParser import ObjRepoParser

def testSqlStatme():
  SummaryID = 23
  tcSteps = "MyTest"
  param1 = "MyParam1"
  param2 = "YourParam2"
  CustomMessage = "This dd"
  Status = "Pass"
  Log.Message("SET NOCOUNT ON; EXEC p_Insert_AutomationExecutionDetail "+ str(SummaryID)+",'"+tcSteps+"','"+""+str(param1)+"~"+str(param2)+"','"+CustomMessage+"','"+Status+"'")
  
  #"SET NOCOUNT ON; EXEC p_Insert_AutomationExecutionDetail "+ str(TestConfig.SummaryID)+"','"+tcSteps+"','"+""+str(param1)+"~"+str(param2)+"','"+CustomMessage+"','"+Status+"'""
def testPath():
  Log.Message(Project.Path + "..\TestInput")
  from Suite import Suite
  ObjSuite = Suite();
  ExcelPath = ObjSuite.GetFilePath("NEWMDBFULLREGQA")
  Log.Message(ExcelPath)

def testDirectDWn():
  directUIHWNDlist = [TCNameMapping.IeDirectUIHWND,TCNameMapping.IeDwndirectUIHWND]
  for dwnBr in directUIHWNDlist:
    if dwnBr.Exists:
      dwnBr.Keys("~S")
def testFileDownload():
  from TestConfig import TestConfig
  ExcelPath = r"C:\aazim\imsautomation5\IMS_Suite\IMS_AutoFramework\TestRepo\TestSuite\MDB.xlsx"
  myExcelVar = ExcelDriver(ExcelPath)
  ObjRecords = myExcelVar.loadWorkSheetIntoMem("MDBObjRep")
  TestConfig.SuiteToRun = StringParser.splitStr(Helper.ReadConfig().get("SuitName"),",")[0]
  TestComplete.TestBrowser = Helper.ReadConfig().get("TESTBROWSER")
  from Suite import Suite
  ObjSuite = Suite();
  OrName = ObjSuite.GetObjectRepositoryName(TestConfig.SuiteToRun);
  TestConfig.ObjRepName = OrName 
  
  xobj = ObjRepoParser(ObjRecords)
  objRepo = ObjRepoParser.getDict(ObjRecords)
  AppURL = Helper.ReadConfig().get("APPURL")
  Page = Helper.ReadConfig().get("PAGEURL")
  ObjBrowser = Sys.Browser()
  TestComplete.ObjPage = ObjBrowser.Page(Page)
  
  ObjWebObject = WebObject();
  ObjSwitch = Switch()
  objSelector = ["querySelector","#exportFiels"]
  ObjSwitch.IMSOperation("EXPORT",objSelector,"LOGREPORT","EXCELNEW");

def testPathsd():
  Log.message(FileIO.getParentDir(""))

def testWebElement2():
  from TestConfig import TestConfig
  TestConfig.IsRenameFile = 0
  from FileIO import FileIO
  FileIO.moveDwnToTemp("EcrBatchReportExecution.log")
  
def testWebElement():
  from TestConfig import TestConfig
  ExcelPath = r"D:\Aazim\IMS_Auto_UI\TestInput\ECR.xlsx"
  myExcelVar = ExcelDriver(ExcelPath)
  ObjRecords = myExcelVar.loadWorkSheetIntoMem("ECRObjRep")
  TestConfig.SuiteToRun = StringParser.splitStr(Helper.ReadConfig().get("SuitName"),",")[0]
  from Suite import Suite
  ObjSuite = Suite();
  OrName = ObjSuite.GetObjectRepositoryName(TestConfig.SuiteToRun);
  TestConfig.ObjRepName = OrName 
  
  xobj = ObjRepoParser(ObjRecords)
  objRepo = ObjRepoParser.getDict(ObjRecords)
  AppURL = Helper.ReadConfig().get("ECRAPPURL")
  Page = Helper.ReadConfig().get("PAGEURL")
  ObjBrowser = Sys.Browser()
  TestComplete.ObjPage = ObjBrowser.Page(Page)
  TestConfig.IsRenameFile = 0
  from ECR import ECR
  ECR.ReadFileLineByLine(r"D:\Aazim\BatchId.txt")
#  ObjWebObject = WebObject();
#  #objSelector = ["querySelector","#exportFiels"]
#  objSelector = ["xpath","//*[@id='dispFormat']/span/span/span[@class='k-input'][text()='Custom']"]
#  
#  #cssSelector = "#alert > div.footer > button"
#  objAct = Action()
#  objAct.ValidateDropDownText(objSelector,"Custom")
#  #objAct.Click(objSelector)
#  
  #GrandTotalSumValue = objAct.Sync(objSelector,Helper.ReadConfig().get("timeout"));
  #Log.Message(GrandTotalSumValue.textContent.strip())


def testPowerShell():
  powerShellComm = "dir " + ConfigReader.useDwnFolder + " -Recurse | Unblock-File"
#  log.Message "Executing Powershell: " + powerShellComm
#  Call Sys.OleObject("WScript.Shell").Run("powershell -command " +powerShellComm)
  Helper.execCLIComm("powershell -command " +powerShellComm)
	
def testFilePath():
  Log.Message(FileIO.getFileExtension(FileIO.getLatestFile(r"C:\Users\aaaazim\Downloads")))
  
def testregex():
  
  errstr = """Invalid value found in file "SampleInput_12.12.2017.3.25.49.PM.xlsx.txt"."""
  pattstr = "^Invalid value found in file \"(.*)\".*"
  Log.Message(StringParser.getFirstMatch(pattstr,errstr))
  
  #function GetReportIDfromFileName(FileName) repComp.svb
  filname = StringParser.getListofAllMatches("_(\d+)[_\.]","ExportExcel_REPORT_22244.66555_2324332.xlsx")
  Log.Message(str(filname))
  
  #Function TrimNewLine(ByVal sString) PlatFormAdminLib.svb
  newStr = """This is crappy test
            and i am not liking it"""
  Log.Message(StringParser.remAllWhiteSpaces(newStr))
  
  #VerGenevaReqDetails(AppDetStr,XlDetStr) PlatFormAdminLib.svb
  rslstr = """sei_netiktran -p 9999-1-00002 -at Incremental -k 05/30/2018:23:59:59  -ac "9999-1-00002.Q12018" --CP yes -f bcp -o GNV_NTK_TRAN_9999-1-00002_Frequent_aazim_CLPD_9999100002Q12018_636638122084205890.bcp"""
  nstr = StringParser.remAllWhiteSpaces(rslstr)
  nstr = StringParser.regexReplace('_\d+\.',nstr,'_.')
  nstr = StringParser.regexReplace('aazim',nstr,'')
  nstr = StringParser.regexReplace('[\d]{2}/[\d]{2}/[\d]{4}',nstr,'')
  Log.Message(nstr)
  
  #findGrandTotSum mdblib.svb
  #FindGrandTotAvg mdblib.svb
  #FindGrandTotMAX mdblib.svb
  #FindGrandTotMin mdblib.svb
  #FindGrandTotCount mdbli.svb
  #FindStdDev mdblib.svb
  #FindMedian mbdlib.svb
  #FindHarmonicMean mdblib.svb
  #FindGeoMean mdblib.svb
  #ValidateCountPercentage mdblib.svb
  nstr = "23.59"
  pattern = "^\d+(\.\d{1,2})?$"
  if(StringParser.testContains(pattern,nstr)):
    Log.Message("Found")
  
  #CleanFiles ECRLib.svb
  lstr = "Consolidated Stmnt xyz "
  pattern1 = "Consolidated Stmnt"
  if(StringParser.testContains(pattern1,lstr)):
    Log.Message("Found")
    
  #ProcessArgs BaseLib.svb
  purl = "https://pilot.imsplatform.seic.com"
  urlPattern = "^(http\:\/\/|https\:\/\/)?([a-z0-9]*.*(pilot)[a-z0-9\-]*.*)\.([a-z0-9][a-z0-9\-].*\.)+[a-z0-9][a-z0-9\-]"
  if(StringParser.testContains(urlPattern,purl)):
    Log.Message("Pilto URL matched")



def TestLogin():
  ObjWebObject = WebObject();
  ObjSwitch = Switch()
  ObjSwitch.IMSOperation("OPENAPP","chrome","https://qa.ims.ea.corp.seic.com","*seic.com*");
  ObjSwitch.IMSOperation("KEYIN",WebObjectHandler.FindWebObject("QUERYSELECTOR;#USERID"),"ajain1"); 
  ObjSwitch.IMSOperation("KEYIN",WebObjectHandler.FindWebObject("QUERYSELECTOR;#PASSWORD"),"Russia@07");
  ObjSwitch.IMSOperation("CLICKBUTTON",WebObjectHandler.FindWebObject("QUERYSELECTOR;#cont"));
    
def TestLaunchChrome():
  ObjAction = Action();
  Log.Message(ObjAction.IgnoreQASteps)
  
def testPandas():
  import site
  site.addsitedir("c:\\Program Files\\Python36\\Lib\\site-packages\\")
  site.addsitedir("D:\\Program_Files\\Anaconda\\Lib\\site-packages")
  import pandas as pd
  from Helper import Helper
  StartTime = Helper.GetCurrentTime();
  xlsx_filename="D:\\Aazim\\IMS_Suite\\IMS_AutoFramework\\TestRepo\\TestSuite\\DDTECRPrivateFund.xlsx"  
  df = pd.read_excel(xlsx_filename, sheetname='TestData')
  Param1 = df.values.tolist()
  header = list(df.columns)
  TestDataRecords = [header] + Param1
  Log.Message("DDT records:" + str(len(TestDataRecords)))
  
  df2 = pd.read_excel(xlsx_filename, sheetname='TestData')
  Param1 = df2.values.tolist()
  header2 = list(df2.columns)
  TCRecords = [header2] + Param1
  Log.Message("Test Step records:" + str(len(TCRecords)))
  ElapsedTime = Helper.GetTimeDiffInSecond(StartTime,Helper.GetCurrentTime())
  Log.Message("Time Taken To Read DDTECRPrivateFund testData: " + str(ElapsedTime))
  
  
  
def Test():
  SQLCommand =  "select id from dbo.portfolio_performance where id = 276596"
  ObjDB = DBConnector();
  #ObjDBConnector = ObjDB.GetConnection("AGDMDLISTQA","netikip")
  ResultList = ObjDB.SelectCommand(SQLCommand,"AGDMDLISTQA","netikip")
  for x in ResultList:
    Log.Message(str(x))
    
def TestInsertCommand():
  SQLCommand =  "SET NOCOUNT ON; EXEC Insert_AutomationExecutionDetail 52,'TC - 01','IMS APPLICATION','IMS APPLICATION','','In Progress'"
  ObjDBConnector = DBConnector("seimdbdevdb2014","Automation_QA");
  ResultList = DBConnector.InsertCommand(SQLCommand)
  Log.Message(ResultList)
  
  
def TestHostName():
  import os

  s= os.getenv('COMPUTERNAME')
  Log.Message(s)
  Log.Message( os.getlogin())
  
def TestUpdateCommand():
  SQLCommand =  "SET NOCOUNT ON;EXEC Update_AutomationExecution "+ aqConvert.VarToStr(1)
  ObjDBConnector = DBConnector("seimdbdevdb2014","Automation_QA");
  DBConnector.UpdateCommand(SQLCommand)

def TestReplace():
  try:
    Log.Message(1/0)
  except Exception as e:
    import sys,os,traceback,inspect,string
    exc_type, exc_value, exc_traceback = sys.exc_info()
    exc_info =(exc_type, exc_value, exc_traceback)
    Log.Message(StringParser.regexReplace(exc_info,'"',"'"))