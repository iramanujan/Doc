from DBConnector import DBConnector
from WebObject import WebObject
import Action
from LoggerHandler import LoggerHandler
from TestConfig import TestConfig
from Helper import Helper
from StringParser import StringParser

class WorkDesk:
  JIRATICKETNUMBER = ""
  LASTCOMMENT = ""
  UPLOADFILENAME = ""
  FILEUPLOADDATE = ""
  
  def __init__(self):
    Log.Message("Initializing WorkDesk Class");
		
  def setJiraTicketNumber(self,PropertyList):
    ObjAction = Action.Action()
    ObjWebObject = WebObject()
    WorkDesk.JIRATICKETNUMBER = ObjAction.GetText(PropertyList)
    TestConfig.SetValeInTempDict("JIRATICKETNUMBER",WorkDesk.JIRATICKETNUMBER)
    if(not StringParser.IsEmptyOrNone(WorkDesk.JIRATICKETNUMBER)):
      LoggerHandler.LogInfo("Pass",CustomMessage="JIRA Ticket Number: ",Parameter1=str(WorkDesk.JIRATICKETNUMBER))
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="JIRA Ticket Number: ",Parameter1=str(WorkDesk.JIRATICKETNUMBER))
      
  def GetJiraTicketNumber(self,PropertyList):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    WebElement = ObjAction.GetObject(WebObject.getPropertyList(PropertyList))
    WebElement.Keys(TestConfig.GetValeFromTempDict("JIRATICKETNUMBER"))
    WebElement.Keys("[Down][Enter]")
    
  def SetUpLoadFileName(self,PropertyList):
    ObjAction = Action.Action()
    ObjWebObject = WebObject()
    WorkDesk.UPLOADFILENAME = ObjAction.GetText(PropertyList)
    TestConfig.SetValeInTempDict("UPLOADFILENAME",WorkDesk.UPLOADFILENAME)
    if(not StringParser.IsEmptyOrNone(WorkDesk.UPLOADFILENAME)):
      LoggerHandler.LogInfo("Pass",CustomMessage="JIRA Ticket Number: ",Parameter1=str(WorkDesk.UPLOADFILENAME))
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="JIRA Ticket Number: ",Parameter1=str(WorkDesk.UPLOADFILENAME))
      
  def GetUpLoadFileName(self,PropertyList):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    WebElement = ObjAction.GetObject(WebObject.getPropertyList(PropertyList))
    WebElement.Keys(TestConfig.GetValeFromTempDict("UPLOADFILENAME"))
    WebElement.Keys("[Down][Enter]")
    
  def SetUpLoadFileDate(self,PropertyList):
    ObjAction = Action.Action()
    ObjWebObject = WebObject()
    WorkDesk.FILEUPLOADDATE = ObjAction.GetText(PropertyList)
    TestConfig.SetValeInTempDict("UPLOADFILENAME",WorkDesk.FILEUPLOADDATE)
    if(not StringParser.IsEmptyOrNone(WorkDesk.FILEUPLOADDATE)):
      LoggerHandler.LogInfo("Pass",CustomMessage="JIRA Ticket Number: ",Parameter1=str(WorkDesk.FILEUPLOADDATE))
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="JIRA Ticket Number: ",Parameter1=str(WorkDesk.FILEUPLOADDATE))
      
  def GetUpLoadFileDate(self,PropertyList):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    WebElement = ObjAction.GetObject(WebObject.getPropertyList(PropertyList))
    WebElement.Keys(TestConfig.GetValeFromTempDict("FILEUPLOADDATE"))
    WebElement.Keys("[Down][Enter]")
      
  def JiraTicketVerifyFromDatabase():
    try: 
      aqString.ListSeparator = "-"
      PrimaryKey     =   aqString.GetListItem(TestConfig.GetValeFromTempDict("JIRATICKETNUMBER"),0)
      IssueNumber    =   aqString.GetListItem(TestConfig.GetValeFromTempDict("JIRATICKETNUMBER"),1)
      
      serverName    = 	Helper.ReadConfig().get("JiraSrvName")
      databaseName	= 	Helper.ReadConfig().get("JiraDbName")
      userName 			=   Helper.ReadConfig().get("JiraDbUser")
      password 			=   Helper.ReadConfig().get("JiraDbPassword")
      sqlCommand    =   "SELECT  JP.pkey, JI.issuenum, * FROM jiraschema.jiraissue  JI  INNER JOIN jiraschema.project  JP ON JP.ID = JI.Project WHERE JI.issuenum = '" + IssueNumber +"' AND JP.pkey = '" + PrimaryKey +"'" 
      aqUtils.Delay(5000,"Validating from Database...")
      OjDBConnector = DBConnector()
      DataSet = OjDBConnector.SelectCommand(sqlCommand,serverName,databaseName,userName,password)
      if(not DataSet):
        LoggerHandler.LogInfo("Failed",CustomMessage="Verify From Database: ",Parameter1 = PrimaryKey,Parameter2 = IssueNumber)
      else:
        LoggerHandler.LogInfo("Pass",CustomMessage="Verify From Database: ",Parameter1 = PrimaryKey,Parameter2 = IssueNumber)
    except Exception as e:
      LoggerHandler.LogInfo("Failed",CustomMessage="Verify From Database: ",Parameter1 = PrimaryKey,Parameter2 = IssueNumber)
       
  def WorkDeskClick(self,PropertyList):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    WebElement = ObjAction.GetObject(PropertyList)
    ObjAction.ScrollIntoView(WebElement);
    WebElement.Click()
     
  def VerifyJIRASearchTicket():
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    LoggerHandler.LogInfo("Info",TestCaseSteps="Enter Jira Ticket in Search Box.",CustomMessage="JIRA Ticket Number: ",Parameter1 = TestConfig.GetValeFromTempDict("JIRATICKETNUMBER"))
    ObjAction.KeyIn(WebObject.getPropertyList("SearchTicket"),str(TestConfig.GetValeFromTempDict("JIRATICKETNUMBER")))
    aqUtils.delay(1000)
    Sys.Desktop.Keys("[Enter]");
    aqUtils.delay(1000)
    keyNo = ObjAction.Sync(WebObject.getPropertyList("keyNo"),TimeOutInMin=Helper.ReadConfig().get("timeout"));
    JiraTicketNum = aqString.Trim(keyNo.textContent, aqString.stAll)
    
    if(JiraTicketNum == TestConfig.GetValeFromTempDict("JIRATICKETNUMBER")):
      LoggerHandler.LogInfo("Pass",TestCaseSteps="Validate JIRA Search",CustomMessage="JIRA Ticket Number: ",Parameter1 = TestConfig.GetValeFromTempDict("JIRATICKETNUMBER"))
    else:
      LoggerHandler.LogInfo("Failed",TestCaseSteps="Validate JIRA Search",CustomMessage="JIRA Ticket Number: ",Parameter1 = TestConfig.GetValeFromTempDict("JIRATICKETNUMBER"))
      
  def VerifyMove():
    CurrentTicketCounter = ""
    MoveNextTicketCounter = ""
    MovePreviousTicketCounter = ""
    CurrentKeyNo = ""
    MoveNextKeyNo = ""
    MovePreviousKeyNo = ""
    
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    
    TicketCounter = ObjAction.Sync(WebObject.getPropertyList("TicketCounter"),TimeOutInMin=Helper.ReadConfig().get("timeout"));
    CurrentTicketCounter = aqString.Trim(TicketCounter.textContent, aqString.stAll)
    
    CrttKeyNo = ObjAction.Sync(WebObject.getPropertyList("keyNo"),TimeOutInMin=Helper.ReadConfig().get("timeout"));
    CurrentKeyNo = aqString.Trim(CrttKeyNo.textContent, aqString.stAll)
    
    aqString.ListSeparator = "-"
    CtNum = aqString.Trim(aqString.GetListItem(CurrentKeyNo,1))
    aqUtils.delay(5000)
    ObjAction.Click(WebObject.getPropertyList("MoveNext"));
    aqUtils.delay(5000)
    
    MoveNextCounter = ObjAction.Sync(WebObject.getPropertyList("TicketCounter"),TimeOutInMin=Helper.ReadConfig().get("timeout"));
    MoveNextTicketCounter = aqString.Trim(MoveNextCounter.textContent, aqString.stAll)
    
    MovNxtKeyNo = ObjAction.Sync(WebObject.getPropertyList("keyNo"),TimeOutInMin=Helper.ReadConfig().get("timeout"));
    MoveNextKeyNo = aqString.Trim(MovNxtKeyNo.textContent, aqString.stAll)
    
    aqString.ListSeparator = "-"
    NextNum = aqString.Trim(aqString.GetListItem(MoveNextKeyNo,1))
    
    LoggerHandler.LogInfo("Info",TestCaseSteps="Current Counter",CustomMessage="Counter: ", Parameter1=str(CurrentTicketCounter))
    LoggerHandler.LogInfo("Info",TestCaseSteps="Current JIRA Ticket",CustomMessage="JIRA Ticket Number: ", Parameter1=CurrentKeyNo)
    LoggerHandler.LogInfo("Info",TestCaseSteps="Next Counter",CustomMessage="Counter: ", Parameter1=MoveNextTicketCounter)
    LoggerHandler.LogInfo("Info",TestCaseSteps="Next JIRA Ticket",CustomMessage="JIRA Ticket Number: ", Parameter1=MoveNextKeyNo)
    
    
    if(int(CurrentTicketCounter) < int(MoveNextTicketCounter)):
      LoggerHandler.LogInfo("Pass",TestCaseSteps="Validate Counter",CustomMessage="Counter Move Next Successfully.")
      if(int(CtNum) < int(NextNum)):
        LoggerHandler.LogInfo("Pass",TestCaseSteps="Validate JIRA Ticket",CustomMessage="JIRA Ticket Move Next Successfully.")
      else:
        LoggerHandler.LogInfo("Pass",TestCaseSteps="Validate JIRA Ticket",CustomMessage="JIRA Ticket Move Next Successfully.")
    else:
      LoggerHandler.LogInfo("Failed",TestCaseSteps="Validate Counter",CustomMessage="Counter Move Next Successfully.")
      
      
    aqUtils.delay(5000)
    ObjAction.Click(WebObject.getPropertyList("MovePrevious"));
    aqUtils.delay(5000)
    
    TicketCounter = ObjAction.Sync(WebObject.getPropertyList("TicketCounter"),TimeOutInMin=Helper.ReadConfig().get("timeout"));
    CurrentTicketCounter = aqString.Trim(TicketCounter.textContent, aqString.stAll)
    
    CrttKeyNo = ObjAction.Sync(WebObject.getPropertyList("keyNo"),TimeOutInMin=Helper.ReadConfig().get("timeout"));
    CurrentKeyNo = aqString.Trim(CrttKeyNo.textContent, aqString.stAll)
    
    aqString.ListSeparator = "-"
    CtNum = aqString.Trim(aqString.GetListItem(CurrentKeyNo,1))
    
    
    LoggerHandler.LogInfo("Info",TestCaseSteps="Current Counter",CustomMessage="Counter: ", Parameter1=str(MoveNextTicketCounter))
    LoggerHandler.LogInfo("Info",TestCaseSteps="Current JIRA Ticket",CustomMessage="JIRA Ticket Number: ", Parameter1=MoveNextKeyNo)
    LoggerHandler.LogInfo("Info",TestCaseSteps="Previous Counter",CustomMessage="Counter: ", Parameter1=CurrentTicketCounter)
    LoggerHandler.LogInfo("Info",TestCaseSteps="Previous JIRA Ticket",CustomMessage="JIRA Ticket Number: ", Parameter1=CurrentKeyNo)
    

    if(int(CurrentTicketCounter) < int(MoveNextTicketCounter)):
      LoggerHandler.LogInfo("Pass",TestCaseSteps="Validate Counter",CustomMessage="Counter Move Previous Successfully.")
      if(int(CtNum) > int(NextNum)):
        LoggerHandler.LogInfo("Pass",TestCaseSteps="Validate JIRA Ticket",CustomMessage="JIRA Ticket Move Previous Successfully.")
      else:
        LoggerHandler.LogInfo("Pass",TestCaseSteps="Validate JIRA Ticket",CustomMessage="JIRA Ticket Move Previous Successfully.")
    else:
      LoggerHandler.LogInfo("Failed",TestCaseSteps="Validate Counter",CustomMessage="Counter Move Previous Successfully.")