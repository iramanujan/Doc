from WebObject import WebObject
from TestComplete import TestComplete
from Helper import Helper
from BulkUpload import BulkUpload
from ECR import ECR
from WebObjectHandler import WebObjectHandler
from FileIO import FileIO
from StringParser import StringParser
from ConfigReader import ConfigReader
from TestConfig import TestConfig
from LoggerHandler import LoggerHandler
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from TCNameMapping import TCNameMapping
from DBConnector import DBConnector

import os

class Action:
  
	Quest = None;
  
	def __init__(self):
		Log.Message("Initializing Action Class");
  
	def OpenApplication(self,PropertyList,URL,Page):
	  TestComplete.OpenBrowser(URL,Page)

	def KeyIn(self,PropertyList,Text):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  WebElement.focus
	  WebElement.value = ""
	  WebElement.Click()
	  Sys.Desktop.Keys(Text);
	
	def KeyInWithOutClean(self,PropertyList,Text):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  WebElement.focus
	  WebElement.Click()
	  Sys.Desktop.Keys(Text);

	def Click(self,PropertyList):
		WebElement = WebObjectHandler.FindWebObject(PropertyList);
		Action.ScrollIntoView(self,WebElement);
		#WebElement.focus
		Log.Message("BEFORECLICK:","", pmHighest, None , Sys.Desktop)
		WebElement.Click() 
		Log.Message("AFTERCLICK:","", pmHighest, None , Sys.Desktop)
	   
	def ClickWithOutScroll(self,PropertyList):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  WebElement.Click() 

	def ClickButton(self,PropertyList):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  WebElement.focus
	  WebElement.ClickButton()
	
	def ClickGo(self,PropertyList):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Log.Message("TBD:- ClickGo");
	  
	def ClickOnXY(self,PropertyList,Coordinates):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Log.Message("TBD:- ClickOnXY");
	  
	def ClickUnCheck(self,PropertyList):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  if (WebElement.checked):
	    WebElement.Click()
	
	def Checked(self,PropertyList,IsCheck):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  WebElement.checked = aqConvert.VarToBool(IsCheck)
	
	def ClickChecked(self,PropertyList,IsCheck):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  WebElement.ClickChecked = aqConvert.VarToBool(IsCheck)

	def ClickCheck(self,PropertyList):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  if(not WebElement.checked):
	    WebElement.Click();
	
	def ClickIfFound(self,PropertyList):
	  WebElement = Action.GetObject(self,PropertyList);
	  if(WebElement is not None or WebElement == "N"):
	    Action.ScrollIntoView(self,WebElement);
	    WebElement.Click();
	
	def Close(self):
	  Helper.closeAllBrowser();
	  
	def ComboBoxIn(self,PropertyList,Value):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  WebElement.click()
	  WebElement.Focus
	  WebElement.Keys(Value)
	  WebElement.Keys("[Down][Enter]")
	  
	def CompareByTextContent(self,PropertyList,Text):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  InputText = Helper.RemoveSpaces(Text)
	  OutputText = Helper.RemoveSpaces(WebElement.textContent)
	  IsMatch = (OutputText == InputText)
	  Log.Message("Pass")if(IsMatch)else Log.Message("Fail")
	
	def DragAndDrop(self,PropertyList,Coordinates):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  aqString.ListSeparator = ":"
	  FromXCoordinates = aqString.GetListItem(Coordinates,0)
	  FromYCoordinates = aqString.GetListItem(Coordinates,1)
	  ToXCoordinates 	 = aqString.GetListItem(Coordinates,2)
	  ToYCoordinates 	 = aqString.GetListItem(Coordinates,3)
	  WebElement.Drag(FromXCoordinates, FromYCoordinates, ToXCoordinates, ToYCoordinates)
	  
	def SelectByVisibleText(self,PropertyList,Value):
		WebElement = WebObjectHandler.FindWebObject(PropertyList);
		try:
				TestComplete.DisableTCLogging(True) 
				Action.ScrollIntoView(self,WebElement);
				TestComplete.DisableTCLogging(False) 
		except:
				Log.Warning("Enable Scroll Into View")
		finally:
				WebElement.ClickItem(Value)
				LoggerHandler.LogInfo("Info",TestCaseSteps="Input Column Name",Parameter1=str(Value))
				LoggerHandler.LogInfo("Info",TestCaseSteps="Move Column",Parameter1=str(WebElement.wSelectedItems))
				Log.Message(WebElement.wSelectedItems)
	  
	  
	def SelectByIndex(self,PropertyList,Index):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  WebElement.ClickItem(aqConvert.StrToInt(Index))
	  
	def SelectByValue(self,PropertyList,VisibleText):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  WebObjId = WebElement.idStr
	  Selector = "#" + WebObjId + " option[value='" + VisibleText + "']"
	  Log.Message(Selector)
	  ChildWebElement = WebElement.QuerySelector(Selector)
	  WebElement.ClickItem(aqString.Trim(ChildWebElement.textContent))
	
	def CleanUp(self):
	  #Log.Message("")
	  Helper.CloseProcess("outlook");
	  
	def SetEnv(self):
	  TestConfig.IsIgnore = 'N';
	  Helper.CloseProcess("excel");
	  
	def GetObject(self,PropertyList):
	  WebElement = WebObject.GetWebElement(PropertyList);
	  return WebElement;
	  
	def GetText(self,PropertyList):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  LoggerHandler.LogInfo("Info",TestCaseSteps="Visible Text of Element: " + str(PropertyList[1]),CustomMessage=WebElement.textContent)
	  return str(WebElement.textContent);
	
	def GetValue(self,PropertyList):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  return WebElement.value;
	  
	def IsDisable(self,PropertyList):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  IsPass = False
	  AttributeValue 					= aqString.ToLower(WebElement.getAttribute("disabled"))
	  Disabled								= aqString.ToLower("disabled")
	  IsPass = (AttributeValue == Disabled)
	  Log.Message("Pass")if(IsPass)else Log.Message("Fail")

	def KeyInRandomEmail(self,PropertyList,Range):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  WebElement.focus
	  WebElement.value = ""
	  WebElement.Click()
	  WebElement.SetText(Helper.GetRandomEmail(Range));
	  
	def KeyInRandomText(self,PropertyList,Range):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  WebElement.focus
	  WebElement.value = ""
	  WebElement.Click()
	  WebElement.SetText(Helper.GetRandomText(Range));
	  
	def KeyInRandomInt(self,PropertyList,Range):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  WebElement.focus
	  WebElement.value = ""
	  WebElement.Click()
	  WebElement.SetText(Helper.GetRandomInt(Range));
	  
	def KeyInText(self,PropertyList):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  WebElement.focus
	  WebElement.value = ""
	  WebElement.Click()
	  WebElement.SetText(Helper.GetText());
	
	def ListItem(self,PropertyList,VisibleText):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  aqUtils.Delay(2000)
	  WebElement.Click()
	  Sys.Desktop.Keys(str(VisibleText));
	  aqUtils.Delay(1000);
	  Sys.Desktop.Keys("[Tab]");
	  aqUtils.Delay(2000);
	  
	def ObjectListItem(self,PropertyList,VisibleText):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  WebElement.Click()
	  WebElement.Keys(aqConvert.VarToStr(VisibleText));
	  aqUtils.Delay(1000);
	  WebElement.Keys("[Tab]");
	  aqUtils.Delay(1000);
	
	def ObjectKeyIn(self,PropertyList,Text):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  Log.Enabled = False
	  WebElement.value = ""
	  Log.Enabled = True
	  WebElement.focus
	  WebElement.Click()
	  WebElement.Keys(Text);
	  Sys.Desktop.Keys("[Tab]")
	  
	def SelectItemByIndex(self,PropertyList,Index):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  WebElement.selectedIndex = aqConvert.StrToInt(Index)
	  WebElement.change();

	def SelectItemByRandomIndex(self,PropertyList,Range):
		WebElement = WebObjectHandler.FindWebObject(PropertyList);
		OldIndexValue = None;
		NewIndexValue = Helper.GetRandomInt(Range);
		if(OldIndexValue == NewIndexValue):
		    NewIndexValue = Helper.GetRandomInt(Range);
		Action.ScrollIntoView(self,WebElement);
		WebElement.selectedIndex = aqConvert.StrToInt(NewIndexValue)
		WebElement.change();
		
	def SetValue(self,PropertyList,Text):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  WebElement.value = aqConvert.VarToStr(Text)
	
	def TerminateBrowser(self):
	  Helper.closeAllBrowser()
	
	def CompareByValue(self,PropertyList,Text):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  InputText = Helper.RemoveSpaces(Text)
	  OutputText = Helper.RemoveSpaces(WebElement.value)
	  IsMatch = (OutputText == InputText)
	  Log.Message("Pass")if(IsMatch)else Log.Message("Fail")
	  
	def Wait(self,PropertyList,Time):
		aqUtils.Delay(aqConvert.StrToInt(Time))
		
	def ReadQuest(self,PropertyList):
		WebElement = Action.GetObject(self,PropertyList);
		if(WebElement is not None or WebElement == "N"):
			self.Quest = "";
			self.Quest = str.strip(WebElement.innerText.split("?")[0])[-1:]*2
			Log.Message(self.Quest)

	def AnsSecQuest(self,PropertyList):
		WebElement = Action.GetObject(self,PropertyList);
		if(WebElement is not None or WebElement == "N"):
		    Action.ScrollIntoView(self,WebElement);
		    WebElement.focus
		    WebElement.value = ""
		    WebElement.Click()
		    WebElement.SetText(self.Quest);
		    LoggerHandler.LogInfo("Info",TestCaseSteps = "Answer of Security Questions",CustomMessage=str(self.Quest),Parameter1="",Parameter2="")
	
	def BrowserDownloadHandler():
	  if(TestComplete.TestBrowser == "iexplore"):
	    return Action.IeDownloadHanlder()
	  else:
	    #chrome directly downloads the file. No handeling required
	    return "directDwn"
	
	def IeDownloadHanlder():
	  TestComplete.DisableTCLogging(True)
	  saveAsButton = TCNameMapping.IeSaveAsBtn
	  TestComplete.DisableTCLogging(False)
	  
	  if (saveAsButton.Exists):
	    saveAsButton.Click
	    return "saveas"
	  else:
	    return "directDwn"
	    
	def Download(DwnFolderPath):
	  #Handle Browser specific objects to start actual download
	  dwnType = Action.BrowserDownloadHandler()
	  
	  if dwnType == "saveas":
	    Helper.DwnSaveAsFile(DwnFolderPath)
	  elif dwnType == "directDwn":
	    FileIO.directDwn(DwnFolderPath)
	  else:
	    Log.Message("Unknown Download Type")
	    
	def DwnAll(PropertyList,parentDir):
	  allLinkObjList =  WebObject.GetWebElement(PropertyList)
	  for link in allLinkObjList:
	    link.click()

	def ECRExportFile(ExpFolderName):
	  #delete all files and sub directories from parent folder
	  MoreLinkPropList = ["querySelector","#summary > div.k-grid-content > table > tbody > tr > td > div > a"]
	  MoreLinkWebObject = WebObject.GetWebElement(MoreLinkPropList)
	  if(not (MoreLinkWebObject is None)):
	    MoreLinkWebObject.Click
	    TestComplete.hardWait(2000)
	    FirstRecJobDetPropList = WebObject.getPropertyList("FirstRcd")
	    FirstRecJobDet = WebObject.GetWebElement(FirstRecJobDetPropList)
	    if (not (FirstRecJobDet is None)):
	      Action.DwnAll(WebObject.getPropertyList("GenLink"),ExpFolderName)
	    else:
	      CloseBtnPropList = WebObject.getPropertyList("CloseButton")
	      CloseBtn = WebObject.GetWebElement(CloseBtnPropList)
	      if (not (CloseBtn is None)):
	        CloseBtn.click()
	        return
	  else:
	    firstRecMessageDetPropList = WebObject.getPropertyList("FirstRcd2")
	    firstRecMessageDet = WebObject.GetWebElement(firstRecMessageDetPropList) 
	    if (not (firstRecMessageDet is None)):
	      Action.DwnAll(WebObject.getPropertyList("GenLink"),ExpFolderName)
	    else:
	      return
	    FileIO.moveDwnToTemp(TestConfig.TestCaseId)
	      
	def GenericExport(self,PropertyList,ExpFolderName):
	  Action.Click(self,PropertyList)
	  
	def ExportFile(self,PropertyList,ExpFileName):
	  from TestConfig import TestConfig
	  #delete all files and sub directories from parent folder
	  parentDir = FileIO.getParentDir(ExpFileName)
	  if(parentDir=="."):
	    parentDir = os.path.join(os.environ['USERPROFILE'],"Downloads")
	  FileIO.emptyDir(parentDir)
	  if TestConfig.TestSuiteName == "DDTECR":
	    Action.ECRExportFile(parentDir)
	  else:
	    Action.GenericExport(self,PropertyList,parentDir)
	  #Download Files in %Userprofile%\Downloads folder or as specified by ExpFileName
	  Action.Download(parentDir)
	  #Calculate the FileName if blank
	  if StringParser.IsEmptyOrNone(ExpFileName) or ExpFileName in ("EXCELNEW","PDF","CSV","ZIP","GEN"):
	    if(TestConfig.SuiteToRun == "NEWMDBFULLREGQA"):
	      fileName = TestConfig.Parameter1;
	      pass
	    else:
	      tcID = TestConfig.TestCaseId
	      #tcName = TestConfig.TestCaseName
	      tcName = StringParser.remAllSpecialCharacters(TestConfig.TestCaseName)
	      fileName = tcID + "_" + tcName
	  else:
	    fileName = ExpFileName  
	  #Once Downloaded move them to project\Temp Folder location
	  FileIO.moveDwnToTemp(fileName)
	
	def Sync(self,PropertyList,TimeOutInMin=Helper.ReadConfig().get("timeout"),checkOverlay="N"):
		if str(TimeOutInMin) in ("0","TxtValue1") or StringParser.isEmpty(str(TimeOutInMin)):
			timeOut = Helper.ReadConfig().get("timeout")
		else:
			timeOut = TimeOutInMin
		return Action.SyncP(self,PropertyList,timeOut,checkOverlay)
	
	
	def SyncP(self,PropertyList,TimeOutInMin,checkOverlay):
	  WebElement = None;
	  Log.Message("Waiting for: " + str(TimeOutInMin) + " mins")
#	  if int(TimeOutInMin) == 0:
#	    TimeOutInMin = Helper.ReadConfig().get("timeout")
	  Spinner =  WebObject.getPropertyList("Spinner");
	  WebObjectHandler.TimeStarted = Helper.GetCurrentTime();
	  WebObjectHandler.TimeElapsed = 0;
	  WebObjectHandler.TimeRemaining = TimeOutInMin
	  Action.WaitTillSpinnerActive(self,Spinner,WebObjectHandler.TimeRemaining,WebObjectHandler.TimeStarted)
	  if(TestConfig.ObjRepName == "MDBObjRep"):
	    if checkOverlay in ("Y","y"):
	      OverlaySpinner =  WebObject.getPropertyList("OverlaySpinner");
	      Action.WaitTillSpinnerActive(self,OverlaySpinner,WebObjectHandler.TimeRemaining,WebObjectHandler.TimeStarted)
	  WebElement = WebObject.GetWebElement(PropertyList);
	  while(WebElement is None):
	    if TestConfig.StopSuite == "Y":
	      Log.Error("Entering SyncP while stopping suite")
	      WebObjectHandler.TimeElapsed = TimeOutInMin
	      return
	    if(WebObjectHandler.TimeElapsed == 3):
	      Log.Message("It's been 3 minutes finding this object, Please check app stat");
	    if(int(WebObjectHandler.TimeElapsed) > int(TimeOutInMin)):
	      return None;
	    Spinner =  WebObject.getPropertyList("Spinner");
	    Action.WaitTillSpinnerActive(self,Spinner,WebObjectHandler.TimeRemaining,WebObjectHandler.TimeStarted)
	    WebElement = WebObject.GetWebElement(PropertyList);
	    WebObjectHandler.TimeElapsed = Helper.GetTimeDiffInMinutes(WebObjectHandler.TimeStarted,Helper.GetCurrentTime());
	    WebObjectHandler.TimeRemaining = int(TimeOutInMin) - int(WebObjectHandler.TimeElapsed)
	    aqUtils.Delay(1000,"Waiting for Obj with Selector: " + PropertyList[1])
	  return WebElement;
	  
	def GetChildElementCount(self,PropertyList):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  WebElement.scrollIntoView(True)
	  return WebElement.childElementCount;
	    
	def SetTempVal(self,PropertyList,Key,param2):
	  if(Key == "CHILDCOUNT"):
	    Value = Action.GetChildElementCount(self,PropertyList);
	    from MDB import MDB
	    MDB.OldColumnCount = Value
	  else:
	    if(param2 == "ByVal"):
	      Value = Action.GetValue(self,PropertyList)
	    else:
	      Value = Action.GetText(self,PropertyList)
	  
	  TestConfig.SetValeInTempDict(Key,Value)
	  
	def GetTempVal(self,Key):
	  Value = TestConfig.GetValeFromTempDict(Key)
	  return Value
	
	def TypeString(self,PropertyList,Value):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  WebElement.setText(str(Value))
	  
	def TypeEmail(self,PropertyList,Value):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  WebElement.Click()
	  Sys.Desktop.Keys(str(Value));
	
	def Report(self,PropertyList,Value):
	  WebElement = Action.GetObject(self,PropertyList);
	  if(WebElement is not None):
	    LoggerHandler.LogInfo("Completed")
	  else:
	    LoggerHandler.LogInfo("Failed")
	    
	    
	def TypeDate(self,PropertyList,Value):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  if(WebElement is not None):
	    if(aqString.ToLower(Value) == "today"):
	      Today 				= datetime.now()
	      Sys.Desktop.Keys(str(Today.strftime('%m/%d/%y')));
	    if(aqString.ToLower(Value) == "yesterday"):
	      Yesterday 		= datetime.now() - timedelta(days=1)
	      Sys.Desktop.Keys(str(Yesterday.strftime('%m/%d/%y')));
	    if(aqString.ToLower(Value) == "tomorrow"):
	      Tomorrow			= datetime.now() + timedelta(days=1)
	      Sys.Desktop.Keys(str(Tomorrow.strftime('%m/%d/%y')));
	    if(aqString.ToLower(Value) == "sixmonths"):
	      SixMonths			= datetime.now() + relativedelta(months=+6)
	      Sys.Desktop.Keys(str(SixMonths.strftime('%m/%d/%y')));
	    
	def WaitTillSpinnerActive(self,PropertyList,TimeOutInMin=Helper.ReadConfig().get("timeout"),StartTimeX=Helper.GetCurrentTime()):
		if isinstance(StartTimeX,str):
			StartTime = Helper.GetCurrentTime()
		else:
			StartTime = StartTimeX
		
		if str(TimeOutInMin) in ("0","TxtValue1","5") or StringParser.isEmpty(str(TimeOutInMin)):
			timeOut = Helper.ReadConfig().get("timeout")
	    
		WebElement = WebObject.GetWebElement(PropertyList);
		while int(WebObjectHandler.TimeElapsed) < int(timeOut) and (WebElement is not None):
		  if TestConfig.StopSuite == "Y":
		    Log.Error("Entering WaitTillSpinnerActive while stopping suite")
		    timeOut = -1
		    return
		  WebElement = WebObject.GetWebElement(PropertyList);
		  if(WebElement is not None):
		    try:
		      if(WebElement.style.CSSText == "display: none;" or WebElement.style.CSSText == "" ):
		        return;
		    except Exception as e:
		      Log.Message(str(e))
		  WebObjectHandler.TimeElapsed = Helper.GetTimeDiffInMinutes(StartTime,Helper.GetCurrentTime());
		  WebObjectHandler.TimeRemaining = int(timeOut) - int(WebObjectHandler.TimeElapsed)
		  aqUtils.Delay(1000,"Waiting till Spinner is Active: " + PropertyList[1])
		
		if(int(WebObjectHandler.TimeElapsed) >= int(TimeOutInMin)):
		  TestConfig.IsIgnore = 'Y'
		  LoggerHandler.LogInfo("Info",CustomMessage="Spinner Activer for too Long time",Parameter1="Spinner still active after " + str(WebObjectHandler.TimeElapsed) + " minutes")
		  return;


	def WaitTillOvelayDivActive(self,PropertyList,TimeOutInMin=Helper.ReadConfig().get("timeout"),StartTimeX=Helper.GetCurrentTime()):
		if isinstance(StartTimeX,str):
			StartTime = Helper.GetCurrentTime()
		else:
			StartTime = StartTimeX
	  
		if str(TimeOutInMin) in ("0","TxtValue1","5") or StringParser.isEmpty(str(TimeOutInMin)):
			timeOut = Helper.ReadConfig().get("timeout")
	  
		WebElement = WebObject.GetWebElement(PropertyList);
		WebObjectHandler.TimeElapsed = 0;
		while int(WebObjectHandler.TimeElapsed) < int(timeOut) and (WebElement is not None):
		  if TestConfig.StopSuite == "Y":
		    Log.Error("Entering WaitTillOverlayDivActive while stopping suite")
		    timeOut = -1
		    return
		  WebElement = WebObject.GetWebElement(PropertyList);
		  if(WebElement is not None):
		    try:
		      if(WebElement.style.CSSText == "display: none;" or WebElement.style.CSSText == "" ):
		        return;
		    except Exception as e:
		      Log.Message(str(e))
		  WebObjectHandler.TimeElapsed = Helper.GetTimeDiffInMinutes(StartTime,Helper.GetCurrentTime());
		  WebObjectHandler.TimeRemaining = int(timeOut) - int(WebObjectHandler.TimeElapsed)
		  aqUtils.Delay(1000,"Waiting till Overlay Div is Active: " + PropertyList[1])
		
		if(int(WebObjectHandler.TimeElapsed) >= int(timeOut)):
		  TestConfig.IsIgnore = 'Y'
		  LoggerHandler.LogInfo("Info",CustomMessage="Overlay Div Spinner Activer for too Long time",Parameter1="Spinner still active after " + str(WebObjectHandler.TimeElapsed) + " minutes")
		  return;	  
		  
		  

	def SelectByVisibleText2(self,PropertyList,Value):
		WebElement = WebObjectHandler.FindWebObject(PropertyList);
		Action.ScrollIntoView(self,WebElement);
		WebElement.ClickItem(Value)
		SelectedValue = Value = aqString.Trim(WebElement.wText,aqString.stAll)
		if(aqString.Trim(Value,aqString.stAll) == aqString.Trim(SelectedValue)):
		  LoggerHandler.LogInfo("Pass",CustomMessage="Validate Dropdown Value:",Parameter1="Expected Selected Value: "+str(Value),Parameter2="Actual Selected Value:"+str(SelectedValue))
		else:
		  TestConfig.IsIgnore = 'Y'
		  LoggerHandler.LogInfo("Failed",CustomMessage="Validate Dropdown Value:",Parameter1="Expected Selected Value: "+str(Value),Parameter2="Actual Selected Value:"+str(SelectedValue))

			
	def ReportTo(self,PropertyList):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  if(WebElement is not None):LoggerHandler.LogInfo("Info",CustomMessage=str(WebElement.textContent))
	  if(WebElement is None):LoggerHandler.LogInfo("Failed",CustomMessage="Fail")

	def TabKeys(self,PropertyList,ParamValue,Param1):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  WebElement.Click()
	  ParamValueList = ParamValue.split(";")
	  LenParamValueList = len(ParamValueList)
	  if(LenParamValueList < 1):return None;
	  else:
	    for Value in ParamValueList:
	     Sys.Desktop.Keys("[Tab]");
	     Sys.Desktop.Keys("^a");
	     Sys.Desktop.Keys("[Del]");
	     Sys.Desktop.Keys(str(Value));

	def ValidateCheckbox(self,PropertyList):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  if(not WebElement.checked):
	    LoggerHandler.LogInfo("Failed",CustomMessage="Validate Checkbox is clicked or not")
	  else:
	    LoggerHandler.LogInfo("Pass",CustomMessage="Validate Checkbox is clicked or not")
	  
	def ValidateDropDownText(self,PropertyList,Text):
	  WebElement = WebObjectHandler.FindWebObject(PropertyList);
	  Action.ScrollIntoView(self,WebElement);
	  if(aqString.Trim(WebElement.textContent) == aqString.Trim(Text)):
	    LoggerHandler.LogInfo("Pass",CustomMessage="Validate Dropdown Text")
	  else:
	    LoggerHandler.LogInfo("Failed",CustomMessage="Validate Dropdown Text",Parameter1=str(aqString.Trim(WebElement.textContent)))
  
	def ScrollIntoView(self,WebElement):
		try:
			WebElement.scrollIntoView(True);
		except Exception as e:
			Log.Message(str(e))
	def ExportToExcel(self,PropertyList,ProcName,FileName):
	  ObjDBConnector = DBConnector();
	  ObjDBConnector.DatabaseToExcel(PropertyList,ProcName,FileName);
	  
	def Pause():
	  Runner.Pause();