from TestComplete import TestComplete
from TestConfig import TestConfig
from Helper import Helper
from WebObject import WebObject
from LoggerHandler import LoggerHandler
import Action
class Login:
	UserName = ""
	Password = ""
  
	kycqa = ""
	Passwordkycqa = ""
  
	kycqa2 = ""
	Passwordkycqa2 = ""
  
	def __init__(self):
		Log.Message("Initializing Login Class");
	
	def IMSLogin(self):
		Helper.closeAllBrowser()
		TestConfig.IsIgnore = "N"
		Log.Message("IMS Login");
		TestComplete.OpenBrowser()
		aqUtils.Delay(3000)
		ObjWebObject = WebObject();
		from Action import Action as RepAct
		ObjAction = RepAct()
		
		if(Login.UserName is None or Login.UserName == ""):
		  Login.UserName = Helper.ReadConfig().get("USER")
		  
		if(Login.Password is None or Login.Password == ""):
		  Login.Password = Helper.ReadConfig().get("PASSWORD")

		ObjUserName = ObjAction.GetObject(WebObject.getPropertyList("UserName"))
		if(ObjUserName is not None):
		  LoggerHandler.LogInfo("Info",TestCaseSteps = "Validate TSU Login Page.",CustomMessage="",Parameter1="",Parameter2="")
		  LoggerHandler.LogInfo("Info",TestCaseSteps = "Application Login By",CustomMessage=Login.UserName,Parameter1="",Parameter2="")
		ObjAction.KeyIn(WebObject.getPropertyList("UserName"),Login.UserName)
		ObjAction.KeyIn(WebObject.getPropertyList("PasswordField"),Login.Password)
		ObjAction.ClickCheck(WebObject.getPropertyList("RegisterThisDevice"))
		ObjAction.ClickIfFound(WebObject.getPropertyList("Login"))
		if(TestComplete.TestBrowser == "chrome"):
		  aqUtils.Delay(10000)
		else:
		  aqUtils.Delay(4000)
		WebElement = ObjAction.GetObject(WebObject.getPropertyList("AnswerSecurityQuestions"))
		#aqUtils.Delay(5000)
		if(WebElement is not None):
		  LoggerHandler.LogInfo("Info",TestCaseSteps = "Security Questions/Answer Page.",CustomMessage="",Parameter1="",Parameter2="")
		  ObjAction.ClickIfFound(WebObject.getPropertyList("AnswerSecurityQuestions"))
		  TestComplete.hardWait(2000)
		  ObjAction.ReadQuest(WebObject.getPropertyList("Question0"))
		  ObjAction.AnsSecQuest(WebObject.getPropertyList("Answer0"))
		  ObjAction.ReadQuest(WebObject.getPropertyList("Question1"))
		  ObjAction.AnsSecQuest(WebObject.getPropertyList("Answer1"))
		  ObjAction.ClickIfFound(WebObject.getPropertyList("Login"))
		#aqUtils.Delay(5000)
		LoggerHandler.LogInfo("Info",TestCaseSteps="Application URL",CustomMessage=TestComplete.ObjPage.URL,Parameter1="",Parameter2="")
		
	def EcrLogin(self):
		Helper.closeAllBrowser()
		TestConfig.IsIgnore = "N"
		Log.Message("ECR Application Login");
		TestComplete.LaunchEcr()
		aqUtils.Delay(5000)
		
	def InSightLogin(self,ParaList,UserType):
		Helper.closeAllBrowser()
		TestConfig.IsIgnore = "N"
		Log.Message("IMS Login");
		TestComplete.OpenBrowser()
		aqUtils.Delay(5000)
		ObjWebObject = WebObject();
		from Action import Action as RepAct
		ObjAction = RepAct()
		if(UserType == "ANALYST"):
		  if((Login.kycqa is None or Login.kycqa == "") and (Login.Passwordkycqa is None or Login.Passwordkycqa == "")) :
		    Login.UserName 		= 	Helper.ReadConfig().get("KYCQA")
		    Login.Password    = 	Helper.ReadConfig().get("KYCQAPASS")
		  else:
		    Login.UserName 		= 	Login.kycqa
		    Login.Password    = 	Login.Passwordkycqa
		if(UserType == "MANAGER"):
		  if((Login.kycqa2 is None or Login.kycqa2 == "") and (Login.Passwordkycqa2 is None or Login.Passwordkycqa2 == "")):
		    Login.UserName 		= 	Helper.ReadConfig().get("KYCQA2")
		    Login.Password		= 	Helper.ReadConfig().get("KYCQAPASS2")
		  else:
		    Login.UserName 		= 	Login.kycqa2
		    Login.Password    = 	Login.Passwordkycqa2

		ObjAction.KeyIn(WebObject.getPropertyList("UserName"),Login.UserName)
		ObjAction.KeyIn(WebObject.getPropertyList("PasswordField"),Login.Password)
		ObjAction.ClickCheck(WebObject.getPropertyList("RegisterThisDevice"))
		ObjAction.ClickIfFound(WebObject.getPropertyList("Login"))
		aqUtils.Delay(10000)
		WebElement = ObjAction.GetObject(WebObject.getPropertyList("AnswerSecurityQuestions"))
		aqUtils.Delay(5000)
		if(WebElement is not None):
		  ObjAction.ClickIfFound(WebObject.getPropertyList("AnswerSecurityQuestions"))
		  TestComplete.hardWait(3000)
		  ObjAction.ReadQuest(WebObject.getPropertyList("Question0"))
		  ObjAction.AnsSecQuest(WebObject.getPropertyList("Answer0"))
		  ObjAction.ReadQuest(WebObject.getPropertyList("Question1"))
		  ObjAction.AnsSecQuest(WebObject.getPropertyList("Answer1"))
		  ObjAction.ClickIfFound(WebObject.getPropertyList("Login"))
		aqUtils.Delay(5000)
