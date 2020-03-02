from TestComplete import TestComplete
from Helper import Helper
from WebObject import WebObject
from StringParser import StringParser
from LoggerHandler import LoggerHandler
from Helper import Helper
from TestConfig import TestConfig
import Action


class WebObjectHandler:
	TimeElapsed = 0;
	TimeRemaining = 0;
	TimeStarted = 0;
  
	def __init__(self):
		Log.Message("Initializing WebObjectHandler Class");
  
	def WaitForDocumentReady():
		IsDocumentReady = False;
		WebObjectHandler.TimeElapsed = 0
		TestComplete.setObjPage()
		ObjPage = TestComplete.ObjPage
		WebObjectHandler.TimeStarted = Helper.GetCurrentTime();
		while((ObjPage.contentDocument is None) or (ObjPage.contentDocument.ReadyState != "complete")):
			if(WebObjectHandler.TimeElapsed > 1):
			  Log.Message("Page Object is not ready")
			  return IsDocumentReady
			ObjPage = TestComplete.ObjPage
			WebObjectHandler.TimeElapsed = Helper.GetTimeDiffInMinutes(WebObjectHandler.TimeStarted,Helper.GetCurrentTime())
			IsDocumentReady = True
		return IsDocumentReady;
	   
	def WaitForObject(PropertyList,TimeOutInMin):
		WebObjectHandler.WaitForDocumentReady()
		from Action import Action as RepAct
		ObjAction = RepAct()
		ObjWebObject = WebObject()
		Spinner = WebObject.getPropertyList("Spinner")
		WebObjectHandler.TimeStarted = Helper.GetCurrentTime();
		WebObjectHandler.TimeElapsed = 0;
		WebObjectHandler.TimeRemaining = TimeOutInMin
		ObjAction.WaitTillSpinnerActive(Spinner,WebObjectHandler.TimeRemaining,WebObjectHandler.TimeStarted)
		if(TestConfig.ObjRepName == "MDBObjRep"):
		  OverlaySpinner = WebObject.getPropertyList("OverlaySpinner")
		  ObjAction.WaitTillSpinnerActive(OverlaySpinner,WebObjectHandler.TimeRemaining,WebObjectHandler.TimeStarted)
		WebElement = None;
		WebElement = WebObject.GetWebElement(PropertyList);
		while(WebElement is None):
		  if TestConfig.StopSuite == "Y":
		    Log.Error("Entering WaitForObject while stopping suite")
		    TimeOutInMin = -1
		    return
		  if(WebObjectHandler.TimeElapsed == 3):
		    Log.Message("It's been 3 minutes finding this object, Please check app stat");
		  if(int(WebObjectHandler.TimeElapsed) > int(TimeOutInMin)):
		    TestConfig.IsIgnore = 'Y'
		    LoggerHandler.LogInfo("Failed",TestCaseSteps="Control not Found: Object = ",Parameter1=PropertyList[0],Parameter2=PropertyList[1])
		    return None;
		  TestComplete.ObjPage.Wait(1500)
		  WebElement = WebObject.GetWebElement(PropertyList);
		  Spinner = WebObject.getPropertyList("Spinner")
		  ObjAction.WaitTillSpinnerActive(Spinner,WebObjectHandler.TimeRemaining,WebObjectHandler.TimeStarted)
		  aqUtils.Delay(1000,"Waiting for Obj with Selector: " + PropertyList[1])
		  WebObjectHandler.TimeElapsed = Helper.GetTimeDiffInMinutes(WebObjectHandler.TimeStarted,Helper.GetCurrentTime());
		  WebObjectHandler.TimeRemaining = int(TimeOutInMin) - int(WebObjectHandler.TimeElapsed)
		return WebElement;
	  
	def WaitForVisibleOnScreen(WebElement):
		try:
			if WebElement.VisibleOnScreen == False:
				Log.Message("Object is not Visible on Screen")
				#aqUtils.Delay(3000,"Waiting for Object to get visible on Screen")
		finally:
			Log.Message("Object does not have VisibleOnScreen property",str(WebElement.outerHTML))
	
	def FindWebObject(PropertyList,TimeOutInMin=Helper.ReadConfig().get("timeout")):
		WebElement = None;
		WebElement = WebObject.GetWebElement(PropertyList);
		if(WebElement is None):
			WebElement = WebObjectHandler.WaitForObject(PropertyList,TimeOutInMin);
			if(WebElement is None):
				TestConfig.IsIgnore = 'Y';
				return None;
		#if(WebElement is not None):
		#	WebObjectHandler.WaitForVisibleOnScreen(WebElement)
		return WebElement;
	  

	def UpdateObjProperty(PropertyList,OldString,NewString):
		from copy import deepcopy
		UpdatedObjProperty = deepcopy(PropertyList);
		UpdatedObjProperty[1] = aqString.Replace(UpdatedObjProperty[1],OldString,NewString);
		return UpdatedObjProperty;
		
	def WaitForWebElementToBeVisible(WebElement):
		WebObjectHandler.TimeElapsed = 0;
		WebObjectHandler.TimeStarted = Helper.GetCurrentTime();
		TimeOutInMin=Helper.ReadConfig().get("timeout")
		while(WebObjectHandler.IsVisible(WebElement)):
			if(int(WebObjectHandler.TimeElapsed) > int(TimeOutInMin)):
				TestConfig.IsIgnore = 'Y'
				return;
			if(WebElement is not None):
				aqUtils.Delay(1000,"Waiting for Obj to be Visible: " + WebElement.outerHTML)
			else:
				aqUtils.Delay(1000,"Waiting for Obj to be found")
			WebObjectHandler.TimeElapsed = Helper.GetTimeDiffInMinutes(WebObjectHandler.TimeStarted,Helper.GetCurrentTime());
		Log.Message("Object visible after " + str(WebObjectHandler.TimeElapsed) + " min.")
	  
	def WaitForWebElementToLeave(WebElement):
		WebObjectHandler.TimeElapsed = 0;
		WebObjectHandler.TimeStarted = Helper.GetCurrentTime();
		TimeOutInMin=Helper.ReadConfig().get("timeout")
		while(WebObjectHandler.IsVisible(WebElement)):
			if(int(WebObjectHandler.TimeElapsed) > int(TimeOutInMin)):
				TestConfig.IsIgnore = 'Y'
				LoggerHandler.LogInfo("Failed",CustomMessage="Object Still Visible after ",Parameter1=str(WebObjectHandler.TimeElapsed),Parameter2="minutes")
				return;
			else:
				aqUtils.Delay(1000,"Waiting for Obj to be Leave: " + WebElement.outerHTML)  
			WebObjectHandler.TimeElapsed = Helper.GetTimeDiffInMinutes(WebObjectHandler.TimeStarted,Helper.GetCurrentTime());
		Log.Message("Object Left after " + str(WebObjectHandler.TimeElapsed) + " minutes")
	    
	def IsVisible(WebElement):
		if(WebElement is None):
			return False;
		else:
			Height = WebElement.offsetHeight
			Width  = WebElement.offsetHeight
		if(Height > 0 or Width > 0):return True;
		else: return False;