import Action
from WebObject import WebObject
from WebObjectHandler import WebObjectHandler
from Helper import Helper
from LoggerHandler import LoggerHandler
from TestConfig import TestConfig
from TestComplete import TestComplete
from StringParser import StringParser
from Helper import Helper
class InSight:
  
  EXTERNALINVESTORID = "";

  ULTBENACCNO = "";
  ULTBENACCNO2 = "";
  
  FUNDMNEMONIC = "";
  FUNDMNEMONIC2 = "";
  
  INVESTORLEGALNAME = "";
  
  def __init__(self):
    Log.Message("Initializing InSight Class");
		
  def GetUpdatedInvestorID(self):
    Log.Message(InSight.ExternalInvestorId);
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    ObjAction.Click(WebObject.getPropertyList("ThirdPartyInvSerchBox"))
    aqUtils.Delay(2000,"Waiting For Search operation to finish")
    TempPropertyList = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("InvestorIdInputListSearchBox"),"INV",InSight.ExternalInvestorId)
    aqUtils.Delay(2000,"Waiting For Search operation to finish")
    ObjAction.Click(TempPropertyList)

  def InvMasterRelationShipVerify(self,PropertyList,Value):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    TempPropertyList = WebObjectHandler.UpdateObjProperty(PropertyList,Value,TestConfig.GetValeFromTempDict("ULTBENACCNO2"))
    WebElement = ObjAction.GetObject(WebObject.getPropertyList(TempPropertyList))
    if(TempPropertyList is not None):
      LoggerHandler.LogInfo("Pass",CustomMessage="Investor Master: ",Parameter1=str(TempPropertyList[1]))
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="Investor Master: ",Parameter1=str(TempPropertyList[1])) 
    aqUtils.Delay(2000) 

  def GetFundMnemonic(self,PropertyList):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    WebElement = ObjAction.GetObject(WebObject.getPropertyList(PropertyList))
    WebElement.Keys(TestConfig.GetValeFromTempDict("FUNDMNEMONIC"))
    WebElement.Keys("[Down][Enter]")

  def SetFundMnemonic(self,PropertyList):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    Value = ObjAction.GetText(WebObject.getPropertyList(PropertyList))
    TestConfig.SetValeInTempDict("FUNDMNEMONIC",Value)
    
  def setFundMnemonic2(self,PropertyList):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    Value = ObjAction.GetText(WebObject.getPropertyList(PropertyList))
    TestConfig.SetValeInTempDict("FUNDMNEMONI2",Value)
    
  def GetFundMnemonic2(self,PropertyList):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    WebElement = ObjAction.GetObject(WebObject.getPropertyList(PropertyList))
    WebElement.Keys(TestConfig.GetValeFromTempDict("FUNDMNEMONIC2"))
    WebElement.Keys("[Down][Enter]")
    
  def SetUltimateBeneficiaryAccountNumber1(self,PropertyList):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    WebElement = ObjAction.GetObject(WebObject.getPropertyList(PropertyList))
    if(WebElement.hasAttribute(value)):
      ULTBENACCNO = WebElement.value;
    else:
      ULTBENACCNO = WebElement.textContent;
    TestConfig.SetValeInTempDict("ULTBENACCNO",ULTBENACCNO)
      
  def GetUltimateBeneficiaryAccountNumber1(self,PropertyList):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    WebElement = ObjAction.GetObject(WebObject.getPropertyList(PropertyList))
    WebElement.Keys(TestConfig.GetValeFromTempDict("ULTBENACCNO"))
    WebElement.Keys("[Down][Enter]")
    
  def SetUltimateBeneficiaryAccountNumber2(self,PropertyList,Range):
    RandText = Helper.GetRandomText(Range)
    TestConfig.SetValeInTempDict("ULTBENACCNO2",RandText)
    WebElement = WebObjectHandler.FindWebObject(PropertyList);
    WebElement.Keys(RandText)
    WebElement.Keys("[Down][Enter]")
      
  def GetUltimateBeneficiaryAccountNumber2(self,PropertyList):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    WebElement = WebObjectHandler.FindWebObject(PropertyList);
    WebElement.Keys(TestConfig.GetValeFromTempDict("ULTBENACCNO2"))
    WebElement.Keys("[Down][Enter]")
      
  def GetInvestorLegalName(self,PropertyList):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    WebElement = ObjAction.GetObject(WebObject.getPropertyList(PropertyList))
    WebElement.Keys(TestConfig.GetValeFromTempDict("INVESTORLEGALNAME"))
    WebElement.Keys("[Down][Enter]")

  def SetInvestorLegalName(self,PropertyList):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    Value = ObjAction.GetText(WebObject.getPropertyList(PropertyList))
    TestConfig.SetValeInTempDict("INVESTORLEGALNAME",Value)
    
  def SetExternalInvestorID(self,PropertyList,Range):
    TestConfig.SetValeInTempDict("EXTERNALINVESTORID",Helper.GetRandomText(Range))
    WebElement = WebObjectHandler.FindWebObject(PropertyList);
    WebElement.Keys(TestConfig.GetValeFromTempDict("EXTERNALINVESTORID"))
    WebElement.Keys("[Down][Enter]")
      
  def GetExternalInvestorID(self,PropertyList):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()
    WebElement = ObjAction.GetObject(WebObject.getPropertyList(PropertyList))
    WebElement.Keys(TestConfig.GetValeFromTempDict("EXTERNALINVESTORID"))
    WebElement.Keys("[Down][Enter]")
     
  def ClickOnLastRecord(self,PropertyList,Param2,Param1):
    ObjWebObject = WebObject();
    ObjAction = Action.Action()

    aqString.ListSeparator = ":"
    TableHeader 					 = aqString.GetListItem(PropertyList[1],0)
    TableBody 					   = aqString.GetListItem(PropertyList[1],1)
    TableLastCell 				 = aqString.GetListItem(PropertyList[1],2)
    
    ColumnPosition = InSight.GetColumnPositionByAttribute(TableHeader,Param1,Param2);
    TableBodyElement = ObjAction.GetObject(WebObject.getPropertyList(TableBody))
    if(TableBodyElement is not None):
      TableBodyChildCount = TableBodyElement.childElementCount
      TempPropertyList1 = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList(TableLastCell),"COLPOS",ColumnPosition)
      TempPropertyList = WebObjectHandler.UpdateObjProperty(TempPropertyList1,"LastRecNo",TableBodyChildCount)
      WebElement = ObjAction.GetObject(TempPropertyList)
      try:
        WebElement.scrollIntoView(True)
      except Exception as e:
        Log.Warning(str(e))
      finally:
        WebElement.Click();
    
  def GetColumnPositionByAttribute(PropertyList,Attribute,ColumnName):
    ColumnTitle = ""
    ObjAction = Action.Action()
    WebElement = ObjAction.GetObject(WebObject.getPropertyList(PropertyList));
    WebElementChildren = WebElement.children
    for index in range ( 0 , WebElement.childElementCount):
      CurrentNode = WebElementChildren.item(index);
      if(CurrentNode.hasAttribute(Attribute)):
        ColumnTitle =  CurrentNode.getAttribute(Attribute)
        if(ColumnName.strip() == ColumnTitle.strip()):
          LoggerHandler.LogInfo("Info",TestCaseSteps="Find Position of Column in Grid.",CustomMessage="Column Position is "+str((index+1)),Parameter1=ColumnName)          
          return (index+1);
    LoggerHandler.LogInfo("Failed",TestCaseSteps="Find Position of Column in Grid.",CustomMessage="Column Position is "+str((index+1)),Parameter1=ColumnName)        
    return 0;
    
  def SetSearchText(self,PropertyList):
    ObjAction = Action.Action()
    WebElement = ObjAction.GetObject(PropertyList);
    TempPropertyList = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList(PropertyList),"TEXT",TestConfig.GetValeFromTempDict("INVESTORLEGALNAME"))
    ObjAction.Sync(TempPropertyList,TimeOutInMin=Helper.ReadConfig().get("timeout"));
    aqUtils.Delay(3000,"Waiting for Investor: "+TestConfig.GetValeFromTempDict("INVESTORLEGALNAME"))
    ObjAction.Click(TempPropertyList);
    
    