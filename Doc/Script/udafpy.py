import math
import copy
from copy import deepcopy
import Action
import os
from WebObject import WebObject
from WebObjectHandler import WebObjectHandler
from Helper import Helper
from LoggerHandler import LoggerHandler
from TestConfig import TestConfig
from TestComplete import TestComplete
from StringParser import StringParser
from FileIO import FileIO
from TestComplete import TestComplete
from TCNameMapping import TCNameMapping
import datetime

class UDF:
  AccountId = ""
  StartDate = ""   
  EndDate = "" 
  UdfScreenName = ""
  UdfTemplatePath =  Project.Path+"\\TestRepo\\UdfTemplates"
  DropLocation = "\\\seimdbqaclas\\FILEDROP\\UDFScreenName"
  EtlInputStore = {}
  EtlFileMapping = {}
  EtlInputCsvFileName = ""


  def __init__(self):
    Log.Message("Initializing UDF Class")
        
  def InitializeLocation(self):
    Log.Message("InitializeUDF")
    self.EtlFileMapping = {
      "AccountClassifications":"Account_classification\\Trigger",
      "InvestmentClassifications":"Investment_Classification\\Trigger",
      "AccountValues":"Account_values\\Trigger",
      "InvestmentValues":"MDSass\\Trigger",
      "InvestorClassifications":"Investor_Classification\\Trigger",
      "InvestorValues":"Investor_Value\\Trigger",
      "RegulatoryInvestmentValues":"RegulatoryInvestmentvalue",
      "SEGOverrides":""
    }
    
  def OpenScreen(self,ParamValue,ScreenName):
    UDF.UdfScreenName = ScreenName
    ObjWebObject = WebObject()
    ObjAction = Action.Action()
    ObjAction.Click(WebObject.getPropertyList("MenuUtilities"))
    RightSubMenuUDFSCREEN = WebObject.getPropertyList("RightSubMenuUDFSCREEN")
    TempPropertyList = WebObjectHandler.UpdateObjProperty(RightSubMenuUDFSCREEN,"UDFSCRNAME",ScreenName)
    ObjAction.Sync(TempPropertyList,TimeOutInMin=Helper.ReadConfig().get("timeout"))
    ObjAction.Click(TempPropertyList)
    ObjAction.Sync(WebObject.getPropertyList("UDFRptTitle"),TimeOutInMin=Helper.ReadConfig().get("timeout"))
    UDFAccFirstChBox = ObjAction.Sync(WebObject.getPropertyList("UDFAccFirstChBox"),TimeOutInMin=Helper.ReadConfig().get("timeout"))
    if(UDFAccFirstChBox is not None):
      LoggerHandler.LogInfo("Pass",TestCaseSteps="Validate "+ScreenName+" UDF Screen",CustomMessage="UDF Screen Opened "+ScreenName+" Successfully.",Parameter1="",Parameter2="")
    else:
      TestConfig.IsIgnore = "Y"
      LoggerHandler.LogInfo("Failed",CustomMessage="Open UDF Screen for",Parameter1=ScreenName)

  def OpenAccount(self,ParamValue,InputList):
    ObjWebObject = WebObject()
    ObjAction = Action.Action()
    aqString.ListSeparator = ";"
    
    UDF.StartDate = aqString.GetListItem(InputList,0)
    UDF.EndDate = aqString.GetListItem(InputList,1)
    UDF.AccountId = aqString.GetListItem(InputList,2)
        
    startdate = UDF.StartDate
    enddate = UDF.EndDate
    accountid = UDF.AccountId

    Log.Message("Account Id " + UDF.AccountId)
    Log.Message("Start Date" + UDF.StartDate)
    Log.Message("End Date" + UDF.EndDate)

    if((Helper.IsDate(startdate)) and Helper.IsDate(enddate)):dateInputCond = "INPUTSTARTendDate"
    if(not Helper.IsDate(startdate) and Helper.IsDate(enddate)):dateInputCond = "INPUTendDate"
    if(not Helper.IsDate(startdate) and (not Helper.IsDate(enddate))):dateInputCond = "SELECTendDate"
    if(not Helper.IsDate(startdate) and not Helper.IsDate(enddate)):dateInputCond = "IGNDATE"

    if(dateInputCond == "INPUTSTARTendDate"):
      aqUtils.Delay(1000,"Enter Start Date for UDF")
      ObjAction.ObjectKeyIn(WebObject.getPropertyList("UDFStartDate"),startdate)
      aqUtils.Delay(1000,"Enter End Date for UDF")
      ObjAction.ObjectKeyIn(WebObject.getPropertyList("UDFEndDate"),enddate)
      
    if(dateInputCond == "INPUTendDate"):
      aqUtils.Delay(5000,"Click on As of Date DropDown")
      ObjAction.ClickWithOutScroll(WebObject.getPropertyList("UDFAsOfDateDropDown"))
      aqUtils.Delay(5000,"Wait for list to appear")
      ObjAction.Sync(WebObject.getPropertyList("UDFAsOfDateDropDownListItemSpecifyDate"),TimeOutInMin=Helper.ReadConfig().get("timeout"))
      aqUtils.Delay(5000,"Select Specify Date List Item")
      ObjAction.Click(WebObject.getPropertyList("UDFAsOfDateDropDownListItemSpecifyDate"))
      
      
      aqUtils.Delay(5000,"Click on As of Date DropDown")
      ObjAction.ClickWithOutScroll(WebObject.getPropertyList("UDFAsOfDateDropDown"))
      aqUtils.Delay(5000,"Wait for list to appear")
      ObjAction.Sync(WebObject.getPropertyList("UDFAsOfDateDropDownListItemSpecifyDate"),TimeOutInMin=Helper.ReadConfig().get("timeout"))
      aqUtils.Delay(5000,"Select Specify Date List Item")
      ObjAction.Click(WebObject.getPropertyList("UDFAsOfDateDropDownListItemSpecifyDate"))
      
      
      aqUtils.Delay(5000,"Enter End Date for UDF")
      ObjAction.ObjectKeyIn(WebObject.getPropertyList("UDFAsOfDate"),enddate)
    
    if(dateInputCond == "SELECTendDate"):
      TempPropertyList = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("UDFAsOfDateDropDownListItemGeneric"),"LISTITEM",endDate)
      ObjAction.Click(WebObject.getPropertyList("UDFAsOfDateDropDown"))
      ObjAction.Sync(WebObject.getPropertyList(TempPropertyList),TimeOutInMin=Helper.ReadConfig().get("timeout"))
      ObjAction.Click(WebObject.getPropertyList(TempPropertyList))
    
    if(dateInputCond == "IGNDATE"):Log.Message("Ignore This condition.")
    
    ObjAction.KeyIn(WebObject.getPropertyList("UDFAccTxtSearch"),accountid)
    ObjAction.Sync(WebObject.getPropertyList("UDFAccListFilterActive"),TimeOutInMin=Helper.ReadConfig().get("timeout"))
    TempPropertyList = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("SearchFilteredAccIDRec"),"ACCOUNTID",accountid)
    SearchFilteredAccIDRec = ObjAction.Sync(TempPropertyList,TimeOutInMin=Helper.ReadConfig().get("timeout"))
    if(SearchFilteredAccIDRec is not None):
      ObjAction.ClickCheck(WebObject.getPropertyList("UDFAccFirstChBox"))
      aqUtils.Delay(10000,"Waiting for Checkbox to get registered")
      ObjAction.ClickCheck(WebObject.getPropertyList("UDFAccFirstChBox"))
      aqUtils.Delay(10000,"Waiting for Checkbox to get registered")
      ObjAction.Click(WebObject.getPropertyList("BtnSubmitRequest"))
      ObjAction.Sync(WebObject.getPropertyList("UDFRptTitle"),TimeOutInMin=Helper.ReadConfig().get("timeout"))
    
    UDFDataGridEditLinkFirstRec = ObjAction.Sync(WebObject.getPropertyList("UDFDataGridEditLinkFirstRec"),TimeOutInMin=Helper.ReadConfig().get("timeout"))
    
    if(UDFDataGridEditLinkFirstRec is not None):
      LoggerHandler.LogInfo("Pass",TestCaseSteps="Open UDF Data Page",CustomMessage = "UDF Data Page Loaded for")
    else:
      TestConfig.IsIgnore = "Y"
      LoggerHandler.LogInfo("Failed",TestCaseSteps="Open UDF Data Page",CustomMessage = "UDF Data Page Loaded for",Parameter1=UDF.UdfScreenName)

  def UIEdit(self,ParamValue,InputList):
    UDF.EnterValIntoFields(self,InputList,"VALID")
    UDF.EnterValIntoFields(self,InputList,"INVALID")

  def EnterValIntoFields(self,WorkFieldList,InputType):
    OrignalCurrentValueDict = {}
    OrignalInputValueDict = {}
    CurrentValueDict = copy.deepcopy(OrignalCurrentValueDict)
    InputValueDict = copy.deepcopy(OrignalInputValueDict)
    UDF.GetCurrentValList(self,WorkFieldList,CurrentValueDict)
        
    UDF.GetInputValList(self,WorkFieldList,InputType,InputValueDict,CurrentValueDict)
    ObjWebObject = WebObject()
    ObjAction = Action.Action()
    ObjAction.Click(WebObject.getPropertyList("UDFDataGridEditLinkFirstRec"))
    ObjAction.Sync(WebObject.getPropertyList("UDFEditFundParamBtnSave"),TimeOutInMin=Helper.ReadConfig().get("timeout"))

    for keys,values in InputValueDict.items():
      Log.Message("Field Name: " + str(keys) + " - Value: " + str(values))
      FieldName 				 = 		 str(keys)
      FieldVal 					 = 		 str(values)
      UDF.EnterVal(self,FieldName,FieldVal)
    Sys.Desktop.Keys("[Tab]");
    ObjAction.Click(WebObject.getPropertyList("UDFEditFundParamBtnSave"))

    if(InputType == "VALID"):
      aqUtils.Delay(5000,"Wait for Alert Window to appear")
      ObjAction.Sync(WebObject.getPropertyList("AlertMessageRecordUpdatedSuccessfully"),TimeOutInMin=Helper.ReadConfig().get("timeout"))
      ObjAction.Click(WebObject.getPropertyList("AlertBtnOk"))
      ObjAction.Sync(WebObject.getPropertyList("UDFDataGridEditLinkFirstRec"),TimeOutInMin=Helper.ReadConfig().get("timeout"))
      UDF.ValidateDataInGrid(self,WorkFieldList,InputValueDict,InputValueDict,InputType)
    else:
      UDF.VerifyInvalidData(self,WorkFieldList,CurrentValueDict,InputValueDict)

  def GetCurrentValList(self,WorkFieldList,CurrentValueDict):
    ParamValueList = WorkFieldList.split(";")
    for Value in ParamValueList:
      FieldName = UDF.GetFieldInfo(self,"FIELD",Value)
      CurrentValue = UDF.GetDataGridFirstRecCellVal(self,FieldName)
      Log.Message("Current Value of Field: " + str(FieldName) + " is: " + str(CurrentValue))
      CurrentValueDict[str(FieldName)] = str(CurrentValue)
    for keys,values in CurrentValueDict.items():
      Log.Message("Field Name: " + str(keys) + " - Value: " + str(values))

  def GetFieldInfo(self,Info,FieldList):
    if(Info == "FIELD"): return FieldList.split(":")[1]
    if(Info == "TYPE"):  return FieldList.split(":")[0]

  def GetDataGridFirstRecCellVal(self,FieldName):
    ObjWebObject = WebObject()
    ObjAction = Action.Action()
    ColumnIndex = UDF.GetColumnPosition(self,WebObject.getPropertyList("UDFDataGridTableHeader"),FieldName);
    TempPropertyList = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("UDFDataGridFirstRecCellValqss"),"COLPOS",ColumnIndex)
    return ObjAction.GetText(TempPropertyList);

  def GetInputValList(self,WorkFieldList,InputType,InputValueDict,CurrentValueDict):
    ParamValueList = WorkFieldList.split(";")
    for Value in ParamValueList:
      FieldName = UDF.GetFieldInfo(self,"FIELD",Value)
      FieldType = UDF.GetFieldInfo(self,"TYPE",Value)
      OrignalValue = CurrentValueDict[FieldName]
      NewValue = Helper.GetRandInput(FieldType,InputType,OrignalValue)
      if(FieldType == "TEXT" and InputType == "INVALID"):
        Log.Message("");
      else:
        InputValueDict[str(FieldName)] = str(NewValue)

  def EnterVal(self,FieldName, FieldVal):
    ObjWebObject = WebObject()
    ObjAction = Action.Action()
    EditParamFieldName = StringParser.RemoveSpaces(FieldName)
    ObjAction.ObjectKeyIn(WebObject.getPropertyList(EditParamFieldName),FieldVal)
    
  def ValidateDataInGrid(self,WorkFieldList,InputValueDict1,InputValueDict2,InputType):
    CellVal = "";
    str = ""
    if(InputType == "INVALID"):
      ParamValueList = WorkFieldList.split(";")
      for Value in ParamValueList:
        FieldName = UDF.GetFieldInfo("FIELD",Value)
        FieldType = UDF.GetFieldInfo("TYPE",Value)
        if(FieldType != "TEXT"):
          str = str + FieldType + ":" + FieldName + ";"
      workFieldList = str[:-1]
    ParamValueList = WorkFieldList.split(";")
    for Value in ParamValueList:
      FieldName = UDF.GetFieldInfo(self,"FIELD",Value)
      FieldType = UDF.GetFieldInfo(self,"TYPE",Value)
      if(FieldType == "DATE"):
        if(InputType == "VALID"):
          UdfObj = UDF()
          CellVal = aqConvert.VarToStr(UDF.GetDataGridFirstRecCellVal(self,FieldName));
        else:
          CellVal = UDF.GetDataGridFirstRecCellVal(self,FieldName)
      else:
          CellVal = UDF.GetDataGridFirstRecCellVal(self,FieldName)
      Log.Message(InputValueDict1[FieldName])
      if(FieldType == "DATE"):
        if(InputType == "VALID"):
          UdfObj = UDF()
          InputVal = UdfObj.ConvertDate(StringParser.RemoveSpaces(InputValueDict1[FieldName]));
      else:
        InputVal = StringParser.RemoveSpaces(InputValueDict1[FieldName])
      LoggerHandler.LogInfo("Info",CustomMessage="updated Value of Field: " + FieldName + " is: " + aqConvert.VarToStr(CellVal))
      LoggerHandler.LogInfo("Info",CustomMessage="Inserted Value of Field: " + FieldName + " is: " + InputVal)
      
      if (CellVal == InputVal):
        LoggerHandler.LogInfo("Pass",CustomMessage=InputType,Parameter1="Field: " + FieldName,Parameter2=" value: " +  InputVal)
      else:
        LoggerHandler.LogInfo("Failed",CustomMessage=InputType,Parameter1="Field: " + FieldName,Parameter2=" value: " +  InputVal)
    
  def VerifyInvalidData(self,WorkFieldList,CurrentValueDict,InputValueDict):
    ObjAction = Action.Action()
    ErrXpath = ""
    EditParamFieldName = ""
    ErrMessage = ""
    ErrTxt = ""
    ErrElem = ""
    CellVal = ""
    ParamValueList = WorkFieldList.split(";")
    for Value in ParamValueList:
      FieldName = UDF.GetFieldInfo(self,"FIELD",Value)
      FieldType = UDF.GetFieldInfo(self,"TYPE",Value)
      if(FieldType != "TEXT"):
        ErrMessage = ""
        EditParamFieldName = StringParser.RemoveSpaces(FieldName) + "_errMsg" ;
        WebElement = ObjAction.Sync(WebObject.getPropertyList(EditParamFieldName),Helper.ReadConfig().get("timeout"));
        InputVal = StringParser.RemoveSpaces(str(InputValueDict.get(FieldName, "")))
        if(WebElement is not None):
          ErrTxt =  WebElement.textContent
          ErrMessage = aqString.Trim(ErrTxt,aqString.stAll)
          LoggerHandler.LogInfo("Pass",CustomMessage="Error Message Shown for Invalid Value in Field: ",Parameter1="Field Name " + FieldName,Parameter2=ErrMessage)
          LoggerHandler.LogInfo("PASS",TestCaseSteps = "Invalid Value in Field" ,CustomMessage=ErrMessage,Parameter1="Field: " + FieldName,Parameter2=" value: " +  InputVal)
        else:
          LoggerHandler.LogInfo("Failed",CustomMessage="Error Message Shown for Invalid Value in Field: ",Parameter1="Field Name " + FieldName,Parameter2=ErrMessage)
          LoggerHandler.LogInfo("Failed",TestCaseSteps = "Invalid Value in Field" ,CustomMessage=ErrMessage,Parameter1="Field: " + FieldName,Parameter2=" value: " +  InputVal)
    
    ObjAction.Click(WebObject.getPropertyList("UDFEditFundParamBtnCancel"))
    ObjAction.Sync(WebObject.getPropertyList("UDFDataGridEditLinkFirstRec"),Helper.ReadConfig().get("timeout"));
    
    ParamValueList = WorkFieldList.split(";")
    for Value in ParamValueList:
      FieldName = UDF.GetFieldInfo(self,"FIELD",Value)
      FieldType = UDF.GetFieldInfo(self,"TYPE",Value)
      if(FieldType != "TEXT"):
        CellVal = UDF.GetDataGridFirstRecCellVal(self,FieldName)
        Log.Message("updated Value of Field: " + FieldName + " is: " + str(CellVal))
        InputVal = StringParser.RemoveSpaces(str(InputValueDict.get(FieldName, "")))
        if(str(CellVal) == str(CurrentValueDict[str(FieldName)])):#InputVal
           Log.Message("Data Validation against Invalid Value for Field: " + FieldName + " Pass")
           LoggerHandler.LogInfo("Pass",CustomMessage="No Change In Data Grid Cell for Field",Parameter1="Field: " + FieldName,Parameter2=" value: " +  InputVal)
        else:
          Log.Message("Data Validation against Invalid Value for Field: " + FieldName + " Fail")
          LoggerHandler.LogInfo("Failed",CustomMessage="No Change In Data Grid Cell for Field",Parameter1="Field: " + FieldName,Parameter2=" value: " +  InputVal)   

  def UdfEtlFileUpload(self,ParamValue,ParamList):
    DownloadFileLocation = ""
    DownloadFileLocation = TestConfig.DownloadFilePath
    LoggerHandler.LogInfo("Info",CustomMessage="ETL File Path",Parameter1=DownloadFileLocation)
    if(FileIO.exist(DownloadFileLocation)):
      WorkFieldList = ParamList
      Log.Message("Fields to be Tested are: " + WorkFieldList)
      UDF.UdfUploadEtlFile(self,DownloadFileLocation,WorkFieldList,"VALID")
    else:
      TestConfig.IsIgnore = "Y"
      ErrMessage = "File not Found at path: " + DownloadFileLocation
      LoggerHandler.LogInfo("Failed",CustomMessage="File Not Found",Parameter1=ErrMessage)
      
  def UdfUploadEtlFile(self,DownloadFileLocation,WorkFieldList,InputType):
    FieldName = ""
    FieldType = ""
    CsvFileName = ""
    TempCurrentValueDict = {}
    TempInputValueDict = {}
    InputValueList = list()
    TempInputValueList = list()
    
    CurrentValueDict = deepcopy(TempCurrentValueDict)
    UDF.GetCurrentValList(self,WorkFieldList,CurrentValueDict);
    
    InputValueDict = deepcopy(TempInputValueDict)
    UDF.GetInputValList(self,WorkFieldList,InputType,InputValueDict,CurrentValueDict);
    
    CsvFileName = ""
    UDF.EtlInputCsvFileName = CsvFileName
    UDF.CreateInputCsv(self,DownloadFileLocation,InputValueDict,InputType,CsvFileName)
    
    KeyUdfScreenName = StringParser.RemoveSpaces(UDF.UdfScreenName)    
    
    InputValueList = deepcopy(TempInputValueList)
    InputValueList.append(str(UDF.AccountId))
    InputValueList.append(str(UDF.StartDate))
    InputValueList.append(str(UDF.EndDate))
    InputValueList.append(TestConfig.DownloadFilePath)
    InputValueList.append(UDF.EtlInputCsvFileName)
    InputValueList.append(CurrentValueDict)
    InputValueList.append(InputValueDict)
    InputValueList.append(WorkFieldList)
    InputValueList.append(InputType)
    
    ObjUdf = UDF();
    ObjUdf.EtlInputStore[KeyUdfScreenName] = InputValueList
    
    ObjAction = Action.Action()
    ObjAction.Click(WebObject.getPropertyList("UDFDataGridBtnSelectFiles"))
    UDF.OpenFile(self,TestConfig.DownloadFilePath)
    ObjAction.Click(WebObject.getPropertyList("ButtonImport"))
    UploadedStatusTick = ObjAction.Sync(WebObject.getPropertyList("UploadedStatusTick"),TimeOutInMin=Helper.ReadConfig().get("timeout"))
    if(UploadedStatusTick is not None):
      LoggerHandler.LogInfo("Pass",CustomMessage="Upload ETL CSV ",Parameter1=InputType,Parameter2=CsvFileName)
    else:
      TestConfig.IsIgnore = "Y"
      LoggerHandler.LogInfo("Failed",CustomMessage="Upload ETL CSV ",Parameter1=InputType,Parameter2=CsvFileName)
      return
      
    ObjAction.Click(WebObject.getPropertyList("UDFDataGridBtnBack"))
    UDFAccFirstRecAccID = ObjAction.Sync(WebObject.getPropertyList("UDFAccFirstRecAccID"),TimeOutInMin=Helper.ReadConfig().get("timeout"))
    
    ObjUdf = UDF()
    ObjUdf.InitializeLocation()
    ServerPath = ObjUdf.EtlFileMapping[StringParser.RemoveSpaces(UDF.UdfScreenName)]
    EtlFileDropLocation = aqString.Replace(ObjUdf.DropLocation,"UDFScreenName",ServerPath)
    
    LoggerHandler.LogInfo("Info",CustomMessage="File location is",Parameter1=EtlFileDropLocation)
    
    if(FileIO.exist(EtlFileDropLocation)):
      LoggerHandler.LogInfo("Pass",CustomMessage="Csv File with " + InputType + " values successfully.",Parameter1=EtlFileDropLocation)
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="Csv File with " + InputType + " values successfully.",Parameter1=EtlFileDropLocation)
      
    TempCurrentValueDict = {}
    TempInputValueDict = {}
    
    CurrentValueDict = deepcopy(TempCurrentValueDict)
    InputValueDict = deepcopy(TempInputValueDict)

  def OpenFile(self,InputCsvFileName):
    FilenameEditBox = None
    ButtonOpen = None 
    OpenFileDialog = None
    if(TestComplete.TestBrowser == "chrome"):
      OpenFileDialog      =   TCNameMapping.GCOpenFileDialog
      FilenameEditBox     =   TCNameMapping.GCFilenameEditBox
      OpenFileDialog      =   TCNameMapping.GCButtonOpen
    if(TestComplete.TestBrowser == "iexplore"):
      OpenFileDialog      =   TCNameMapping.IEOpenFileDialog
      FilenameEditBox     =   TCNameMapping.IEFilenameEditBox
      OpenFileDialog      =   TCNameMapping.IEButtonOpen
    
    Counter = 0  
    while(not OpenFileDialog.Exists):
      if(int(Counter) > 60):
        ErrMessage = OpenFileDialog.WndCaption + " not found. Uploading Failed for File: " + InputCsvFileName
        TestConfig.IsIgnore = "Y"
        LoggerHandler.LogInfo("Failed",CustomMessage=ErrMessage,Parameter1=InputCsvFileName)
        return
      aqUtils.Delay(1000,"Waiting For " + OpenFileDialog.WndCaption + " Dialog");
      Counter =  Counter + 1
      
    if(OpenFileDialog.Exists):
      FilenameEditBox.Click(98, 6)
      FilenameEditBox.SetText("")
      FilenameEditBox.SetText(InputCsvFileName)
      OpenFileDialog.ClickButton()
    else:
      ErrMessage = OpenFileDialog.WndCaption + " not found. Uploading Failed for File: " + InputCsvFileName
      TestConfig.IsIgnore = "Y"
      LoggerHandler.LogInfo("Failed",CustomMessage=ErrMessage,Parameter1=InputCsvFileName)
      return
      
  def VerifyETLUpdate(self,ParamValue,ScreenName):
    OriginalExpFileName = None;
    UploadedFileName = None;
    EtlCurrentValueDict = {};
    EtlInputValueDict = {};
    InputValueListListOfInputValues = list()
    
    TempEtlCurrentValueDict = {};
    TempEtlInputValueDict = {};
    TempInputValueList = list()
    
    EtlCurrentValueDict   =   deepcopy(TempEtlCurrentValueDict)
    EtlInputValueDict     =   deepcopy(TempEtlInputValueDict)
    InputValueList        =   deepcopy(TempInputValueList)
    
    AccountId = None;
    StartDate = None;
    EndDate = None;
    WorkFieldList = None;
    InputType = None;
    
    UdfScreenName = StringParser.RemoveSpaces(ScreenName)
    ObjUdf = UDF()
    InputValueList = ObjUdf.EtlInputStore[UdfScreenName]
    
    AccountId             =     InputValueList[0]
    StartDate             =     InputValueList[1]
    EndDate               =     InputValueList[2]
    OriginalExpFileName   =     InputValueList[3]
    UploadedFileName      =     InputValueList[4]
    EtlCurrentValueDict   =     InputValueList[5]
    EtlInputValueDict     =     InputValueList[6]
    WorkFieldList         =     InputValueList[7]
    InputType             =     InputValueList[8]
    
    for key, value in EtlCurrentValueDict.items():
      Log.Message("Field Name: " + str(key) + " - Value: " + str(value))
      LoggerHandler.LogInfo("Info",CustomMessage="ETL Current Value Dict",Parameter1=key,Parameter2=value)
      
    for key, value in EtlInputValueDict.items():
      Log.Message("Field Name: " + str(key) + " - Value: " + str(value))
      LoggerHandler.LogInfo("Info",CustomMessage="ETL Input Value Dict",Parameter1=key,Parameter2=value)
      

    ObjUdf.InitializeLocation()
    ServerPath = ObjUdf.EtlFileMapping[StringParser.RemoveSpaces(UDF.UdfScreenName)]
    EtlFileDropLocation = aqString.Replace(ObjUdf.DropLocation,"UDFScreenName",ServerPath)
    LoggerHandler.LogInfo("Info",CustomMessage="ETL Drop Location",Parameter1=EtlFileDropLocation)
    
    Counter = 0;
    if(FileIO.IsFileExist(EtlFileDropLocation)):
      while(FileIO.IsFileExist(EtlFileDropLocation)):
        if(int(Counter) > 240):
          TestConfig.IsIgnore = "Y"
          ErrMessage = "Took too long to run ETL"
          LoggerHandler.LogInfo("Failed",CustomMessage="Time OUT",Parameter1=ErrMessage)
        aqUtils.Delay(1000,"Waiting for ETL to pickup file from path:  " + EtlFileDropLocation)    
    #else:
      #aqUtils.Delay(240000,"Waiting 4 mins for ETL to finish")
      
    ObjUdf = UDF();  
    if(InputType == "VALID"):
      ObjUdf.ValidateDataInGrid(WorkFieldList,EtlInputValueDict,EtlInputValueDict,InputType);
    else:
      ObjUdf.ValidateDataInGrid(WorkFieldList,EtlInputValueDict,EtlInputValueDict,InputType);
          
    EtlCurrentValueDict   =   deepcopy(TempEtlCurrentValueDict)
    EtlInputValueDict     =   deepcopy(TempEtlInputValueDict)
    InputValueList        =   deepcopy(TempInputValueList)
   
  def CreateInputCsv(self,DownloadFileLocation,InputValueDict,InputType,CsvFileName):
    now = datetime.datetime.now()
    Log.Message( str(now.strftime("%m%d%Y%I%M%S")))
    TempCsvValueDict ={}
    CsvValueDict = deepcopy(TempCsvValueDict)
    Header = "";
    FirstRecord = ""
    with open(DownloadFileLocation,'r') as f:
      Header 						= f.readline()
      FirstRecord 			= f.readline()
    
    aqString.ListSeparator = ","
    for i in range(0, aqString.GetListLength(Header)):
      ColumnName 			                    =     aqString.GetListItem(Header,i)
      ColumnValue 		                    =     aqString.GetListItem(FirstRecord,i)
      CsvValueDict[ColumnName]						=			ColumnValue
      Log.Message("Column Name: "+ColumnName+" Column Value "+ColumnValue)
      LoggerHandler.LogInfo("Info",TestCaseSteps="CSV File Column Name and Value",CustomMessage=ColumnName,Parameter1=ColumnValue);
      
    for key in InputValueDict:
      Log.Message("Element " + key + " Old Val: " + str(CsvValueDict[key]) + " New Val:" + str(InputValueDict[key]))
      CsvValueDict[key] = str(InputValueDict[key])
      LoggerHandler.LogInfo("Info",TestCaseSteps="Update Value in CSV By",CustomMessage=str(key),Parameter1=str(InputValueDict[key]));
      
    NewHeader 					= "";
    NewFirstRecord 			= ""
    
    for key in CsvValueDict:
      NewHeader 						= NewHeader + key + ","  
      NewFirstRecord 				= NewFirstRecord + str(CsvValueDict[key]) + ","
      
    DestFilePath = DownloadFileLocation.split(".")[0]+"#"+str(now.strftime("%m%d%Y%I%M%S"))+"."+DownloadFileLocation.split(".")[1]
    os.rename(DownloadFileLocation, DestFilePath)
    UDF.EtlInputCsvFileName = DestFilePath.split("#")[0]+"."+DestFilePath.split(".")[1]
      
    file = open(UDF.EtlInputCsvFileName,"w")
    file.write(NewHeader[:-1]) 
    file.write(NewFirstRecord[:-1]) 
    file.close()  
      
  def GetColumnPosition(self,PropertyList,ColumnName):
    ColumnTitle = ""
    ObjAction = Action.Action()
    WebElement = ObjAction.GetObject(PropertyList);
    WebElementChildren = WebElement.children
    for index in range ( 0 , WebElement.childElementCount):
      CurrentNode = WebElementChildren.item(index);
      if(CurrentNode.hasAttribute("data-title")):
        ColumnTitle =  CurrentNode.getAttribute("data-title")
        if(ColumnName.strip() == ColumnTitle.strip()):
          LoggerHandler.LogInfo("Info",TestCaseSteps="Find Position of Column in Grid.",CustomMessage="Column Position is "+str((index+1)),Parameter1=ColumnName)          
          return (index+1);
    LoggerHandler.LogInfo("Failed",TestCaseSteps="Find Position of Column in Grid.",CustomMessage="Column Position is "+str((index+1)),Parameter1=ColumnName)  
    
  def ConvertDate(self,InputDate):
    date = aqString.SubString(InputDate,0,10)
    mm = date.split("/")[0]
    if(int(mm) < 10):
      mm = "0"+str(mm)
    
    dd = date.split("/")[1]
    if(int(dd) < 10):
      dd = "0"+str(dd)
    
    yy = date.split("/")[2]
    Log.Message(mm+"-"+dd+"-"+yy)
    return mm+"-"+dd+"-"+yy