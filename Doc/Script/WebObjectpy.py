from TestComplete import TestComplete
from inspect import signature
from By import By
from ObjRepoParser import ObjRepoParser

class WebObject:
	
	def __init__(self):
		Log.Message("Initializing WebObject Class");

	def GetWebElement(PropertyList):
	    FindBy    = None;
	    Property1 = None;
	    Property2 = None;
	    Property3 = None;
	    
	    FindBy = PropertyList[0];
	    Property1 = PropertyList[1];

	    if(len(PropertyList) == 3):
	      Property2 = PropertyList[2];
	    if(len(PropertyList) == 4):
	      Property3 = PropertyList[3];
	    
	    ObjBy = By();
	    SelectBy = ObjBy.SelectorType.get(aqString.ToUpper(FindBy), lambda: "Invalid Operation");
	    ObjSignature = signature(SelectBy)
	    ParamLength = len(ObjSignature.parameters) 
	    if(ParamLength == 1):
	        return SelectBy(Property1)
	    elif(ParamLength == 2):
	        return SelectBy(Property1,Property2)
	    elif(ParamLength == 3):
	        return SelectBy(Property1,Property2,Property3)
	
	def getPropertyList(aliasName):
	  return ObjRepoParser.objRepo[aliasName]