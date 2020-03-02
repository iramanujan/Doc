import site
site.addsitedir(Project.Path+"TestRepo\\PyPackages")
import sys
import pyodbc
from TestConfig import TestConfig
from Helper import Helper
import pandas as pd
import os, datetime
from DBConnector import DBConnector


class LoggerHandler:
  ServerName    = 								Helper.ReadConfig().get("AutoSrvName")
  DatabaseName	= 								Helper.ReadConfig().get("AutoDbName")
  SuitName			=									TestConfig.SuiteToRun
  
    
  def InsertAutomationExecution():
    from TestConfig import TestConfig
    from StringParser import StringParser
    if(TestConfig.URL is not None):
      Url = TestConfig.URL
    else:
      Url= Helper.ReadConfig().get("APPURL")
      
    Log.Message(Url)
    ObjLoggerHandler = LoggerHandler();
    SQLCommand = None;
    SQLCommand =  "SET NOCOUNT ON; EXEC p_Insert_AutomationExecution '"+ aqConvert.VarToStr(TestConfig.SuiteToRun) +"','"+Helper.GetHostName()+"','"+Helper.GetLoginUser()+"','In Progress','"+Url+"'"
    TestConfig.Execution_Id = ObjLoggerHandler.InsertCommand(SQLCommand)
    if TestConfig.Execution_Id == 0:
      TestConfig.StopSuite = "Y"
      raise Exception("Previous Execution is still in Progress")
    del ObjLoggerHandler
    
  def InsertAutomationExecutionSummary():
    ObjLoggerHandler = LoggerHandler();
    SQLCommand = None;
    SQLCommand =  "SET NOCOUNT ON; EXEC p_Insert_AutomationExecutionSummary "+ aqConvert.VarToStr(TestConfig.Execution_Id)+",'"+aqConvert.VarToStr(TestConfig.TestCaseId)+"','"+aqConvert.VarToStr(TestConfig.TestCaseSteps)+"','','Info'"
    TestConfig.SummaryID = ObjLoggerHandler.InsertCommand(SQLCommand)
    del ObjLoggerHandler
    
  def UpdateAutomationExecutionSummary(Status):
    ObjLoggerHandler = LoggerHandler();
    SQLCommand = None;
    SQLCommand =  "SET NOCOUNT ON; EXEC p_Update_AutomationExecutionSummary "+aqConvert.VarToStr(TestConfig.SummaryID)+",'"+Status+"',''"
    ObjLoggerHandler.UpdateCommand(SQLCommand)
    del ObjLoggerHandler
    
  def UpdateAutomationExecution(status):
    ObjLoggerHandler = LoggerHandler();
    SQLCommand = None;
    SQLCommand =  "SET NOCOUNT ON;EXEC p_Update_AutomationExecution "+ aqConvert.VarToStr(TestConfig.Execution_Id)+",'"+status
    ObjLoggerHandler.UpdateCommand(SQLCommand)
    del ObjLoggerHandler
     
  def InsertCommand(Connection,SQLCommand):
    try:
      ObjLoggerHandler = LoggerHandler();
      Connection  = pyodbc.connect("Driver={SQL Server};Server="+ObjLoggerHandler.ServerName+";Database="+ObjLoggerHandler.DatabaseName+";Trusted_Connection=yes;")
      cursor = Connection.cursor()
      cursor.execute(SQLCommand)
      Rows = cursor.fetchone()
      cursor.commit()
      return Rows[0]
    except Exception as E:
      tb = sys.exc_info()[2]
      Log.Message(SQLCommand)
      Log.Message(str(E.with_traceback(tb)))
    finally:
      cursor.close();
      del cursor
      del ObjLoggerHandler
      Connection.close()
      
  def UpdateCommand(Connection,SQLCommand):
    try:
      ObjLoggerHandler = LoggerHandler();
      Connection  = pyodbc.connect("Driver={SQL Server};Server="+ObjLoggerHandler.ServerName+";Database="+ObjLoggerHandler.DatabaseName+";Trusted_Connection=yes;")
      cursor = Connection.cursor()
      cursor.execute(SQLCommand)
      cursor.commit()
    except Exception as E:
      tb = sys.exc_info()[2]
      Log.Message(str(E.with_traceback(tb)))
    finally:
      cursor.close();
      del cursor
      del ObjLoggerHandler
      Connection.close()
		
  def LogInfo(Status,TestCaseSteps="",CustomMessage="", Parameter1="",Parameter2=""):
    
    ObjLoggerHandler = LoggerHandler();
    ObjLoggerHandler.SaveLogInText(TestCaseSteps+"|"+CustomMessage+"|"+Parameter1+"|"+Parameter2)
    tcSteps = TestConfig.TestCaseSteps if(TestCaseSteps is None or TestCaseSteps == "") else TestCaseSteps
    param1 = TestConfig.Parameter1 if(Parameter1 is None or Parameter1 == "") else Parameter1
    param2 = TestConfig.Parameter2 if(Parameter2 is None or Parameter2 == "") else Parameter2
    SQLCommand = None;
    SQLCommand =  "SET NOCOUNT ON; EXEC p_Insert_AutomationExecutionDetail "+ str(TestConfig.SummaryID)+",'"+tcSteps+"','"+""+str(param1)+"~"+str(param2)+"','"+CustomMessage+"','"+Status+"'"
    TestConfig.DetailID = ObjLoggerHandler.InsertCommand(SQLCommand)
    del ObjLoggerHandler

  def SaveLogInText(self,LogData):
    from FileIO import FileIO
    FileIO.createDir(TestConfig.TempLocation)
    FileLocation =  Project.Path+"\\TestRepo\\TempFiles\\Logger.txt"
    FileIO.WriteTextIntoFile(FileLocation,LogData)
	
  def ExportTestResultIntoExcel():
    ServerName    = 								Helper.ReadConfig().get("AutoSrvName")
    DatabaseName	= 								Helper.ReadConfig().get("AutoDbName")
    ObjDBConnector = DBConnector();
    TestConfig.TRLocation = Project.Path+Helper.ReadConfig().get("SourceLocation")+"\\TestResult_"+TestConfig.SuiteToRun+"_"+datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')+".xlsx";
    SQLCommand = "SELECT * FROM v_AutomationExecutionDetails WHERE Execution_Id = " + str(TestConfig.Execution_Id)
    Connection = ObjDBConnector.GetConnection(ServerName,DatabaseName,None,None)
    DataSet = pd.read_sql(SQLCommand,Connection)
    DataHeaderList = list(DataSet)
    for Header in DataHeaderList:
      DataSet[Header] = DataSet[Header].astype(str)
    DataSet.to_excel(TestConfig.TRLocation,sheet_name = TestConfig.SuiteToRun,index = False)