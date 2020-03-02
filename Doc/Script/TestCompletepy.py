from Helper import Helper
from LoggerHandler import LoggerHandler
from TestConfig import TestConfig
class TestComplete:
  ObjPage = None
  TestBrowser = ""
  AppURL      = ""
  
  def __init__(self):
    Log.Message("Initializing TestComplete Class")
    
  def setObjPage():
    Page = Helper.ReadConfig().get("PAGEURL")
    ObjBrowser = Sys.Browser()
    TestComplete.ObjPage = ObjBrowser.Page(Page)
  
  def OpenBrowser():
    Page 																	 = Helper.ReadConfig().get("PAGEURL")
    if(TestComplete.TestBrowser is None or TestComplete.TestBrowser == ""):
      TestComplete.AppURL = Helper.ReadConfig().get("APPURL")
      TestConfig.URL = TestComplete.AppURL 
    if(TestComplete.TestBrowser is None or TestComplete.TestBrowser == ""):
      TestComplete.TestBrowser = Helper.ReadConfig().get("TESTBROWSER")

    if(TestComplete.TestBrowser == "iexplore"):
      TestComplete.LaunchIE(TestComplete.TestBrowser,TestComplete.AppURL,Page);
    elif(TestComplete.TestBrowser == "chrome"):
      TestComplete.LaunchChrome(TestComplete.TestBrowser,TestComplete.AppURL,Page);
    else:
      Log.Message("")
    
  def LaunchChrome(BrowserName,URL,Page):
    LoggerHandler.LogInfo("Info",TestCaseSteps="Browser version: ",CustomMessage=aqConvert.VarToStr(Browsers.Item[BrowserName].Version),Parameter1=BrowserName)
    LoggerHandler.LogInfo("Info",TestCaseSteps="Browser Description: ",CustomMessage=Browsers.Item[BrowserName].Description,Parameter1=BrowserName)
    Browsers.Item[BrowserName].RunOptions = "--incognito --disable-session-crashed-bubble --disable-infobars --disable-password-generation --clear-token-service --ignore-autocomplete-off-autofill";
    Browsers.Item[BrowserName].Run(URL);
    #Log Browser version
    Log.Message("Browser version: " + aqConvert.VarToStr(Browsers.Item[BrowserName].Version));
    #Log Browser Description:
    Log.Message("Browser Description: " + Browsers.Item[BrowserName].Description);
    #Maximize Browser
    ObjBrowser = Sys.Browser()    
    ObjBrowser.BrowserWindow(0).Maximize()
    TestComplete.ObjPage = ObjBrowser.Page(Page)
         
  def LaunchIE(BrowserName,URL,Page):
    LoggerHandler.LogInfo("Info",TestCaseSteps="Browser version: ",CustomMessage=aqConvert.VarToStr(Browsers.Item[BrowserName].Version),Parameter1=BrowserName)
    LoggerHandler.LogInfo("Info",TestCaseSteps="Browser Description: ",CustomMessage=Browsers.Item[BrowserName].Description,Parameter1=BrowserName)
    Browsers.Item[BrowserName].Run(URL);
    #Log Browser version
    Log.Message("Browser version: " + aqConvert.VarToStr(Browsers.Item[BrowserName].Version));
    #Log Browser Description:
    Log.Message("Browser Description: " + Browsers.Item[BrowserName].Description);
    #Maximize Browser
    ObjBrowser = Sys.Browser()    
    ObjBrowser.BrowserWindow(0).Maximize()
    #Handle website’s security certificate.
    TestComplete.ObjPage = ObjBrowser.Page(Page)
    try:
      Overridelink = TestComplete.ObjPage.EvaluateXPath("//a[@id='overridelink']")
      if(Overridelink is not None):
        Overridelink[0].Click();
        aqUtils.Delay(2000)
      else:
        Overridelink = TestComplete.ObjPage.EvaluateXPath("//a[@id='overridelink']")
        if(Overridelink is not None):
          Overridelink[0].Click()
    except Exception as e:
      Log.Message(str(e))
      
  def LaunchEcr():
    BrowserName							 =	 "chrome"
    if(TestComplete.TestBrowser is None or TestComplete.TestBrowser == ""):
      TestComplete.TestBrowser = 	 Helper.ReadConfig().get("TESTBROWSER")
      BrowserName							 =	 "chrome"
    
    URL 										 = Helper.ReadConfig().get("ECRAPPURL")
    Page 										 = Helper.ReadConfig().get("PAGEURL")
    LoggerHandler.LogInfo("Info",TestCaseSteps="Browser version: ",CustomMessage=aqConvert.VarToStr(Browsers.Item[BrowserName].Version),Parameter1=BrowserName)
    LoggerHandler.LogInfo("Info",TestCaseSteps="Browser Description: ",CustomMessage=Browsers.Item[BrowserName].Description,Parameter1=BrowserName)
    Browsers.Item[BrowserName].RunOptions = "--incognito --disable-session-crashed-bubble --disable-infobars --disable-password-generation --clear-token-service --ignore-autocomplete-off-autofill";
    Browsers.Item[BrowserName].Run(URL);
    #Log Browser version
    Log.Message("Browser version: " + aqConvert.VarToStr(Browsers.Item[BrowserName].Version));
    #Log Browser Description:
    Log.Message("Browser Description: " + Browsers.Item[BrowserName].Description);
    #Maximize Browser
    ObjBrowser = Sys.Browser()    
    ObjBrowser.BrowserWindow(0).Maximize()
    TestComplete.ObjPage = ObjBrowser.Page(Page)
          
  
  
  def IsValidateObjectProperty(WebElement,PropertyType,Condition):
    #Enabled, Exists, Visible, disabled
    return aqObject.CheckProperty(WebElement, PropertyType, cmpEqual, Condition)
  
  def DisableTCLogging(truthCond):
    Log.Enabled = (not truthCond)
  
  def hardWait(timeInMilliSec,WaitMessage=None):
    if WaitMessage is not None:
      aqUtils.Delay(timeInMilliSec,WaitMessage)
    
  def refreshPage():
    Sys.Browser(TestComplete.TestBrowser).Page("*").Keys("[F5]")
    