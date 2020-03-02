import math
import Action
from WebObject import WebObject
from WebObjectHandler import WebObjectHandler
from Helper import Helper
from LoggerHandler import LoggerHandler
from TestConfig import TestConfig
from TestComplete import TestComplete
from StringParser import StringParser
from Helper import Helper
class MDB:
  InqNum = "";
  OldColumnCount = None;
  NewColumnCount = None;

  def __init__(self):
    Log.Message("Initializing MDB Class");
		
  def OpenReport(self,IsReopen,ParamValue,Param1):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    ObjAction.Click(WebObject.getPropertyList("ExpandReportExplorer"))
    LoggerHandler.LogInfo("Info",TestCaseSteps="Click On Expand Report Explorer")
    ObjAction.Sync(WebObject.getPropertyList("TitleCloseExplorer"),2)
    if(aqConvert.VarToInt(Param1) == 0):
      Value = aqString.Trim(TestConfig.GetValeFromTempDict("GETREPORTID"),aqString.stAll)
      aqString.ListSeparator = ":"
      MDB.InqNum = aqString.Trim(aqString.GetListItem(Value,1),aqString.stAll)
      Log.Message("Search for Report ID: " + str(MDB.InqNum))
      PropertyList = WebObject.getPropertyList("TextBoxReportSearch");
      ObjAction.KeyIn(PropertyList,MDB.InqNum)
      TempPropertyList = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("LinkReport"),"RepIDCol",MDB.InqNum)
      ObjAction.Click(TempPropertyList)
      try:
        WebElement = ObjAction.GetObject(WebObject.getPropertyList("OverlayCancelButton"))
        if(WebElement is not None):
          WebElement.scrollIntoViewIfNeededIfNeeded(True)
          WebElement.Click();
          WebElement = ObjAction.GetObject(WebObject.getPropertyList("OverlayCancelButton"))
          if(WebElement is not None):
            WebElement.scrollIntoViewIfNeededIfNeeded(True)
            WebElement.Click();
        LoggerHandler.LogInfo("Info",TestCaseSteps = "Click On Cancel Button")
      except Exception as e:
        LoggerHandler.LogInfo("Warning",TestCaseSteps="Click On Cancel Button",CustomMessage = str(e))
        Log.Warning(str(e))
    else:
      ParamValueList = ParamValue.split(";")
      LenParamValueList = len(ParamValueList)
      if(LenParamValueList < 1):
        return None;
      else:
        for Value in ParamValueList:
          MDB.EnterReportParam(str(Value))
  
  def EnterReportParam(ReportParam):
    ObjAction = Action.Action()
    ObjWebObject = WebObject()
    ObjWebObjectHandler = WebObjectHandler();
    
    ReportParamList = ReportParam.split("=")
    if(len(ReportParamList) == 2):
      ParamName 	= 			 aqString.ToLower(aqString.Trim(ReportParamList[0]))
      ParamValue 	= 			 aqString.Trim(ReportParamList[1])
      if(ParamName == "repid"):
        RepId = ParamValue;
        PropertyList = WebObject.getPropertyList("TextBoxReportSearch");
        ObjAction.KeyIn(PropertyList,RepId)
        LoggerHandler.LogInfo("Info",TestCaseSteps="Enter Report Id in Search Box.",Parameter1=RepId,Parameter2="")
        TempPropertyList = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("LinkReport"),"RepIDCol",RepId)
        ObjAction.Click(TempPropertyList)
        LoggerHandler.LogInfo("Info",TestCaseSteps="Select Report from Left navigation",Parameter1=RepId,Parameter2="")
        try:
          aqUtils.Delay(5000,"Wait For Cancel Button")
          WebElement = WebObject.GetWebElement(WebObject.getPropertyList("OverlayCancelButton"))
          if(WebElement is not None):
            WebElement.Click();
            WebElement = WebObject.GetWebElement(WebObject.getPropertyList("OverlayCancelButton"))
            if(WebElement is not None):
              WebElement.Click();
          LoggerHandler.LogInfo("Info",TestCaseSteps = "Click On Cancel Button",CustomMessage="",Parameter1="",Parameter2="")
        except Exception as e:
          LoggerHandler.LogInfo("Warning",TestCaseSteps="Click On Cancel Button",CustomMessage = str(e))
          Log.Warning(str(e))
        InqNumId = ObjAction.GetText(WebObject.getPropertyList("RepID"))  
        LoggerHandler.LogInfo("Info",TestCaseSteps="Log Report INQ Number",CustomMessage=aqString.Trim(InqNumId),Parameter1=aqString.Trim(RepId),Parameter2="")
        ObjAction.Sync(WebObject.getPropertyList("DataGridFirstLoadFirstRec"),TimeOutInMin=Helper.ReadConfig().get("timeout"),checkOverlay="N") 
        #aqUtils.Delay(7000,"Waiting Extra Time for spinner to go away")
      if(ParamName == "accno"):
        Account = ParamValue;
        aqUtils.Delay(2000,"Wait For "+str(Account))
        ObjAction.KeyIn(WebObject.getPropertyList("ComboBoxAccountSearch"),Account)
        TempPropertyList = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("AccSearchListItem"),"AccNoCol",Account)
        ObjAction.Sync(TempPropertyList,TimeOutInMin=Helper.ReadConfig().get("timeout"))
        ObjAction.Click(TempPropertyList);
        LoggerHandler.LogInfo("Info",TestCaseSteps="Enter Account Number.",Parameter1=Account,Parameter2="")
      if(ParamName == "startdate"):
        StartDate = ParamValue;
        ObjAction.KeyIn(WebObject.getPropertyList("DateControlStartDate"),StartDate)
        LoggerHandler.LogInfo("Info",TestCaseSteps="Enter Start Date",Parameter1=StartDate,Parameter2="")
      if(ParamName == "enddate"):
        EndDate = ParamValue;
        PropertyList = WebObject.getPropertyList("DateControlEndDate");
        ObjAction.KeyIn(PropertyList,EndDate)
        LoggerHandler.LogInfo("Info",TestCaseSteps="Enter End Date",Parameter1=EndDate,Parameter2="")
      if(ParamName == "valuationdate"):
        ValuationDate = ParamValue;
        PropertyList = WebObject.getPropertyList("ValuationDate");
        ObjAction.KeyIn(PropertyList,ValuationDate)
        LoggerHandler.LogInfo("Info",TestCaseSteps="Enter Valuation Date",Parameter1=ValuationDate,Parameter2="")
      if(ParamName == "tradedate"):
        TradeDate = ParamValue;
        PropertyList = WebObject.getPropertyList("TradeDate");
        ObjAction.KeyIn(PropertyList,TradeDate)
        LoggerHandler.LogInfo("Info",TestCaseSteps="Enter Trade Date",Parameter1=TradeDate,Parameter2="")
      if(ParamName == "clientgroup"):
        ClientGroup = ParamValue;
        PropertyList = WebObject.getPropertyList("DropDownClientGroup");
        ObjAction.Click(PropertyList)
        ObjAction.Sync(WebObject.getPropertyList("ListBoxClientGroupDropDown"),TimeOutInMin=Helper.ReadConfig().get("timeout"))
        TempPropertyList = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("ListItemClientGroupGeneric"),"LISTITEM",ClientGroup)
        ObjAction.Click(TempPropertyList);
        LoggerHandler.LogInfo("Info",TestCaseSteps="Slect Client Group",Parameter1=ClientGroup,Parameter2="")
      if(ParamName == "repbasis"):
        ReportBasis = ParamValue;
        PropertyList = WebObject.getPropertyList("DropDownReportBasis");
        ObjAction.ListItem(PropertyList,ReportBasis)
        LoggerHandler.LogInfo("Info",TestCaseSteps="Slect Report Basis",Parameter1=ReportBasis,Parameter2="")
      if(ParamName == "currver"):
        CurrentVersion = ParamValue;
        PropertyList = WebObject.getPropertyList("CurrentVersionDrpDwn");
        ObjAction.ListItem(PropertyList,CurrentVersion)
        LoggerHandler.LogInfo("Info",TestCaseSteps="Slect Current Version",Parameter1=CurrentVersion,Parameter2="")
      if(ParamName == "prevver"):
        PreviousVersion = ParamValue;
        PropertyList = WebObject.getPropertyList("PrevVersDrpDwn");
        ObjAction.ListItem(PropertyList,PreviousVersion)
        LoggerHandler.LogInfo("Info",TestCaseSteps="Slect Previous Version",Parameter1=PreviousVersion,Parameter2="")
      if(ParamName == "client"):
        Client = ParamValue;
        PropertyList = WebObject.getPropertyList("ClientDrpDwn");
        ObjAction.ListItem(PropertyList,Client)
        LoggerHandler.LogInfo("Info",TestCaseSteps="Slect Client",Parameter1=Client,Parameter2="")
      if(ParamName == "apptype"):
        AppType = ParamValue;
        PropertyList = WebObject.getPropertyList("AppTypeDrpDwn");
        ObjAction.ListItem(PropertyList,AppType)
        LoggerHandler.LogInfo("Info",TestCaseSteps="Slect Application Type",Parameter1=AppType,Parameter2="")
      if(ParamName == "reptype"):
        ReportType = ParamValue;
        PropertyList = WebObject.getPropertyList("RepTypeDrpDwn");
        ObjAction.ListItem(PropertyList,ReportType)
        LoggerHandler.LogInfo("Info",TestCaseSteps="Slect Report Type",Parameter1=ReportType,Parameter2="")
        
  def ValidateAddRemoveColumn(self,PropertyList, IsAdd):
    ObjAction = Action.Action()
    WebElement = ObjAction.Sync(PropertyList,5);
    if(WebElement is not None):
      MDB.NewColumnCount = WebElement.childElementCount;
      Log.Message("New Column Count is :"+str(MDB.NewColumnCount));
      Log.Message("Old Column Count is :"+str(MDB.OldColumnCount));
      if(str(IsAdd) == "1"):
        if(int(MDB.NewColumnCount) > int(MDB.OldColumnCount)):
          LoggerHandler.LogInfo("Info",TestCaseSteps="Column Count, Before Add New Column",CustomMessage=str(MDB.OldColumnCount))
          LoggerHandler.LogInfo("Info",TestCaseSteps="Column Count, After Add New Column" ,CustomMessage=str(MDB.NewColumnCount)) 
          LoggerHandler.LogInfo("Pass","Validate Add Column.",CustomMessage=str("Before Add Column Count = "+str(MDB.OldColumnCount)+"; "+"After Add Column Count = "+str(MDB.NewColumnCount)))
        else:
          LoggerHandler.LogInfo("Failed","Validate Add Column.",CustomMessage=str("Before Add Column Count = "+str(MDB.OldColumnCount)+"; "+"After Add Column Count = "+str(MDB.NewColumnCount)))
      if(str(IsAdd) == "0"):
        if(int(MDB.NewColumnCount) < int(MDB.OldColumnCount)):
          LoggerHandler.LogInfo("Info",TestCaseSteps="Column Count, Before Remove New Column" ,CustomMessage=str(MDB.NewColumnCount))
          LoggerHandler.LogInfo("Info",TestCaseSteps="Column Count, After Remove New Column",CustomMessage=str(MDB.OldColumnCount))
          LoggerHandler.LogInfo("Pass","Validate Remove Column.",CustomMessage=str("Before Remove Column Count = "+str(MDB.OldColumnCount)+"; "+"After Remove Column Count = "+str(MDB.NewColumnCount)))
        else:
          LoggerHandler.LogInfo("Failed","Validate Remove Column.",CustomMessage=str("Before Remove Column Count = "+str(MDB.OldColumnCount)+"; "+"After Remove Column Count = "+str(MDB.NewColumnCount)))
    else:
      LoggerHandler.LogInfo("Failed",TestCaseSteps="Validate Add/Remove Column.",CustomMessage="Validate Add/Remove Column failed")
               
  def ValidateGrandTotalSum(self,PropertyList,ColumnName):
    try:
      ObjAction = Action.Action()
      WebElement = ObjAction.Sync(WebObject.getPropertyList("DataGridFirstRec"),Helper.ReadConfig().get("timeout"));
      GrandTotalSumValue = MDB.GetGrandTotalSum(ColumnName);
      aqString.ListSeparator = ":"
      SumText = aqString.GetListItem(GrandTotalSumValue,0)
      SumVal = abs(float(aqString.Replace(aqString.GetListItem(GrandTotalSumValue,1),",","")))
      Log.Message("Sum Text: " + SumText + " Sum Value: " + str(SumVal))
      LoggerHandler.LogInfo("Info",TestCaseSteps="Grand Sub Total Value: ",CustomMessage=str(GrandTotalSumValue),Parameter1=ColumnName)
      LoggerHandler.LogInfo("Info",TestCaseSteps="Sum Text: ",CustomMessage=str(SumText),Parameter1=ColumnName)
      LoggerHandler.LogInfo("Info",TestCaseSteps="Sum Value: ",CustomMessage=str(SumVal),Parameter1=ColumnName)
      if(SumText.strip() == "Sum"):
        if (StringParser.TextContains("^\d+(\.\d{1,2})?$",str(SumVal))):
          LoggerHandler.LogInfo("Pass","Validate Grand Sub Total Functionality",CustomMessage=str(SumVal),Parameter1=ColumnName)
        else:
          LoggerHandler.LogInfo("Failed",TestCaseSteps="Validate Grand Sub Total Functionality for:",Parameter1=ColumnName)
      else:
        LoggerHandler.LogInfo("Failed",TestCaseSteps="Validate Grand Sub Total Functionality for:",Parameter1=ColumnName)
      del ObjAction
    except Exception as e:
      LoggerHandler.LogInfo("Failed",TestCaseSteps="Validate Grand Sub Total Functionality for:",Parameter1=ColumnName,Parameter2="")

  def GetGrandTotalSum(ColumnName):
    ObjAction = Action.Action()
    ColumnPosition = MDB.GetColumnPosition(WebObject.getPropertyList("TableHeaderElement"),ColumnName)
    if(ColumnPosition == 0):return False;
    SumCellSelector = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("GrantTotalSumFieldValue"),"ColPos",ColumnPosition)
    GrandTotalSumValue = ObjAction.Sync(SumCellSelector,Helper.ReadConfig().get("timeout"));
    return GrandTotalSumValue.textContent.strip() 
   
  def GetColumnPosition(PropertyList,ColumnName):
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
    return 0;

  def ValidateFilter(self,PropertyList,InputParams):
    try:
      Result = False;
      ObjAction = Action.Action()
      aqString.ListSeparator = ":"
      FilterColumnName = aqString.GetListItem(InputParams, 0)
      FilterCondition = aqString.GetListItem(InputParams, 1)
      FilterValue = aqString.Trim(aqString.GetListItem(InputParams, 2))
      ColumnPosition = MDB.GetColumnPosition(WebObject.getPropertyList("TableHeaderElement"),FilterColumnName)
      if(ColumnPosition == 0): return False;
      WebElement = ObjAction.Sync(WebObject.getPropertyList("TableBodyElement"),Helper.ReadConfig().get("timeout")); 
      if(WebElement is not None):
        WebElementChildElementCount = WebElement.childElementCount
        WebElementChildren = WebElement.children
        for index in range(0,WebElementChildElementCount):
          GrandChildren = WebElementChildren.item(index).children;
          CellValue = str(GrandChildren.item(ColumnPosition-1).textContent)         
          if(FilterCondition == "EQUAL"):
            if(eval(str(FilterValue != aqString.Replace(CellValue,",","")))):
              Result = True;
          if(FilterCondition == "GREATERTHAN"):
            if(eval(str(float(FilterValue) >= float(aqString.Replace(CellValue,",",""))))):
              Result = True;
          if(FilterCondition =="LESSTHAN"):
            if(eval(str(float(FilterValue) <= float(aqString.Replace(CellValue,",",""))))):
              Result = True;
        if(Result):
          LoggerHandler.LogInfo("Failed",TestCaseSteps="Validate Filter Functionality",CustomMessage="Different Record Found At: Position" + str(index+1) + "; Value: " + CellValue, Parameter1=InputParams)
        else:
          LoggerHandler.LogInfo("Pass",TestCaseSteps="Validate Filter Functionality", Parameter1=InputParams)
    except Exception as e:
      LoggerHandler.LogInfo("Failed",TestCaseSteps="Validate Filter Functionality",CustomMessage=str(e), Parameter1=InputParams, Parameter2="")
        
  def ValidateDynamicFilter(self,PropertyList,InputParams):
    Result = False;
    ObjAction = Action.Action()
    aqString.ListSeparator = ":"
    FilterColumnName1 		 = 		aqString.GetListItem(InputParams, 0)
    FilterCondition 			 = 		aqString.GetListItem(InputParams, 1)
    FilterColumnName2 		 = 		aqString.GetListItem(InputParams, 2)

    ColumnPosition1 = MDB.GetColumnPosition(WebObject.getPropertyList("TableHeaderElement"),FilterColumnName1)
    if(ColumnPosition1 == 0): return False

    ColumnPosition2 = MDB.GetColumnPosition(WebObject.getPropertyList("TableHeaderElement"),FilterColumnName2)
    if(ColumnPosition2 == 0): return False

    WebElement = ObjAction.Sync(WebObject.getPropertyList("TableBodyElement"),Helper.ReadConfig().get("timeout")) 

    if(WebElement is not None):
        WebElementChildElementCount = WebElement.childElementCount
        WebElementChildren = WebElement.children
        for index in range(0,WebElementChildElementCount):
          GrandChildren = WebElementChildren.item(index).children
          CellValue1 = str(GrandChildren.item(ColumnPosition1 - 1).textContent)
          CellValue2 = str(GrandChildren.item(ColumnPosition2 - 1).textContent)
          if(FilterCondition == "EQUAL"):
            if(eval(CellValue1) != eval(CellValue2)):
              Result = True
            if(FilterCondition == "GREATERTHAN"):
              if(eval(CellValue1) <= eval(CellValue2)):
                Result = True
            if(FilterCondition == "LESSTHAN"):
              if(eval(CellValue1) >= eval(CellValue2)):
                Result = True
        if(Result):
          LoggerHandler.LogInfo("Failed",TestCaseSteps="Validate Dynamic Filter Functionality",CustomMessage="Different Record Found At: Position" + str(index+1) + "; Value: " + CellValue, Parameter1=InputParams)
        else:
          LoggerHandler.LogInfo("Pass",CustomMessage="Validate Filter Functionality", Parameter1=InputParams)

  def ValidateRepotVisibleOnDashboard(self,PropertyList):
    ObjAction = Action.Action()
    IsRepotVisible = False
    TempPropertyList = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("DashBoardRepTitle"),"REPID",MDB.InqNum)
    WebElement = ObjAction.Sync(TempPropertyList,TimeOutInMin=Helper.ReadConfig().get("timeout"))
    if(WebElement is not None) :
      LoggerHandler.LogInfo("Pass",CustomMessage="Validate Repot Visible On Dashboard")
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="Validate Repot Visible On Dashboard")
    del ObjAction
    
  def ValidateSorting(self,PropertyList,InputParams):
    ObjAction = Action.Action()
    FisrtValseAsc = None
    FisrtValseDesc = None

    LastValueAsc = None
    LastValueDesc = None
    LoggerHandler.LogInfo("Info",CustomMessage="Validate Sorting",Parameter1=InputParams)
    #Proceed only if data is loaded on the grid
    WebElement = ObjAction.GetObject(WebObject.getPropertyList("DataGridVisibleRecordCount"))
    if(WebElement is not None):
        if(WebElement.textContent == "No items to display"):
            return False

    aqString.ListSeparator = ":"
    ColumnType = aqString.GetListItem(InputParams,0)
    ColumnName = aqString.GetListItem(InputParams,1)
    

    if(ColumnType == "numeric"): 
        ObjPropertySuffix = " > div" 
    else: 
        ObjPropertySuffix = ""

    ColumnPosition = MDB.GetColumnPosition(WebObject.getPropertyList("TableHeaderElement"),ColumnName)
    MDB.SetSortOrder(ColumnName, "RadButtonLevel1SortDesc")
    ResultSet1 = MDB.GetFirstAndLastValue(ColumnPosition,ColumnName,ObjPropertySuffix)
    if(ResultSet1 == ""):
        Log.Error("")
    else:
        aqString.ListSeparator = ":"
        FisrtValseDesc = StringParser.RemoveSpaces(aqString.GetListItem(ResultSet1, 0))#-----
        LastValueDesc = StringParser.RemoveSpaces(aqString.GetListItem(ResultSet1, 1))#-----
    MDB.SetSortOrder(ColumnName, "RadButtonLevel1SortAsc")
    ResultSet2 = MDB.GetFirstAndLastValue(ColumnPosition,ColumnName,ObjPropertySuffix)
    if(ResultSet2 == ""):
        Log.Error("")
    else:
        aqString.ListSeparator = ":"
        FisrtValseAsc 				 = 		StringParser.RemoveSpaces(aqString.GetListItem(ResultSet2, 0))
        LastValueAsc 					 = 		StringParser.RemoveSpaces(aqString.GetListItem(ResultSet2, 1))

    #Log.Message("Min Value: " + str(FisrtValseAsc) + " Max Value: " + str(LastValueAsc))
    LoggerHandler.LogInfo("Info",TestCaseSteps="Values After Apply Desc. Sorting",CustomMessage="Fisrt Valse Desc:|" + str(FisrtValseDesc)+ "|, Last Value Desc:|" + str(LastValueDesc), Parameter1=InputParams)
    LoggerHandler.LogInfo("Info",TestCaseSteps="Values After Apply Asc.  Sorting",CustomMessage="Fisrt Valse Asc:|" + str(FisrtValseAsc)+ "|, Last Value Asc.:|" + str(LastValueAsc), Parameter1=InputParams)
    Log.Message("Fisrt Valse Desc:|" + str(FisrtValseDesc) + "|, Last Value Asc:|" + str(LastValueAsc) + "|, Last Value Desc:|" + str(LastValueDesc) + "|,  Fisrt Valse Asc:|" + str(FisrtValseAsc) + "|")
    if(eval(str(str(FisrtValseDesc) == str(LastValueAsc))) and eval(str(str(FisrtValseAsc)  == str(LastValueDesc)))):
        LoggerHandler.LogInfo("Pass",TestCaseSteps="Validate Sorting",Parameter1=InputParams)
    else:
        LoggerHandler.LogInfo("Failed",TestCaseSteps="Validate Sorting",Parameter1=InputParams)

  def SetSortOrder(ColumnName,SortOrderObjectAlias):
    ObjAction = Action.Action()
    ObjAction.Click(WebObject.getPropertyList("ButtonEditReport"))
    aqUtils.Delay(10000,"Wait for edit window to load")
    #WebElement = ObjAction.GetObject(WebObject.getPropertyList("ButtonOK"))
    
    ObjAction.Click(WebObject.getPropertyList("EditWinOptionSort"))
    UnlockSortingCheckbox = ObjAction.GetObject(WebObject.getPropertyList("UnlockSortingCheckbox"))
    if(UnlockSortingCheckbox is not None):
        if(not UnlockSortingCheckbox.checked):
            ObjAction.Click(WebObject.getPropertyList("UnlockSortingCheckbox"))
            
    ObjAction.ListItem(WebObject.getPropertyList("DropDownLevel1SortSelect"),ColumnName)
    ObjAction.Click(WebObject.getPropertyList(SortOrderObjectAlias))
    ObjAction.Click(WebObject.getPropertyList("ButtonOK"))
    aqUtils.Delay(5000,"Wait for edit window to leave")
    ObjAction.Sync(WebObject.getPropertyList("DataGridFirstRec"),TimeOutInMin=Helper.ReadConfig().get("timeout"))

  def GetFirstAndLastValue(ColumnPosition,ColumnName,ObjPropertySuffix):
    tempSelector= []
    del tempSelector[:]
    tempSelector.clear()
    ObjAction = Action.Action()
    tempSelector = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("FirstCellElement"),"ColPosition",ColumnPosition)
    tempSelector[1] = tempSelector[1] + ObjPropertySuffix
    fieldXpath = tempSelector
    Log.Message("Xpath for first element: " + str(fieldXpath[1]))
    firstVal = ObjAction.GetText(fieldXpath)
    DataGridGoToLastPage = ObjAction.GetObject(WebObject.getPropertyList("DataGridGoToLastPage"))
    if(DataGridGoToLastPage is not None):
        DataGridGoToLastPage.Click()
        aqUtils.Delay(6000,"Waiting for Grid to load")
        ObjAction.Sync(WebObject.getPropertyList("DataGridFirstRec"),TimeOutInMin=Helper.ReadConfig().get("timeout"))
    TableBodyElement = ObjAction.Sync(WebObject.getPropertyList("TableBodyElement"),TimeOutInMin=Helper.ReadConfig().get("timeout"))
    if(TableBodyElement is not None):
        TableBodyChildElementCount = TableBodyElement.childElementCount
        tempSelector = "";
        tempSelector = WebObjectHandler.UpdateObjProperty(WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("LastCellEelement"),"ColPosition",ColumnPosition),"LastRecNo",TableBodyChildElementCount)
        tempSelector[1] = tempSelector[1] + ObjPropertySuffix
        fieldSelector = tempSelector
        LastVal = ObjAction.GetText(fieldSelector)
    else:
        return ""
    tempSelector = None;
    return firstVal + ":" + LastVal