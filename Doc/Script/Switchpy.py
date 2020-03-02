from inspect import signature
from Action import Action
from KeyWord import KeyWord

class Switch:
  ObjKeyWord = None;
  
  def __init__(self):
    Log.Message("Initializing Switch Class");
    if(self.ObjKeyWord is None):
      self.ObjKeyWord = KeyWord();
     
  def IMSOperation(self,ActionName,PropertyList,Param1=None,Param2=None,Param3=None,Param4=None):
    from TestConfig import TestConfig
    if TestConfig.SuiteType == "DDT":
      Arg1 = Param1
      Arg2 = Param2
    else:
      Arg1 = Param2
      Arg2 = Param1
    Operation = self.ObjKeyWord.Case.get(aqString.ToUpper(ActionName), lambda: "Invalid Operation")
    ObjSignature = signature(Operation)
    ParamLength =  len(ObjSignature.parameters)
    if(ParamLength == 0):
      Operation()
    if(ParamLength == 1):
      Operation(self)
    elif(ParamLength == 2):
      Operation(self,PropertyList)
    elif(ParamLength == 3):
      Operation(self,PropertyList,Arg1)
    elif(ParamLength == 4):
      Operation(self,PropertyList,Arg1,Arg2)
    elif(ParamLength == 5):
      Operation(self,PropertyList,Arg1,Arg2,Param3)
    elif(ParamLength == 6):
      Operation(self,PropertyList,Arg1,Arg2,Param3,Param4)
    