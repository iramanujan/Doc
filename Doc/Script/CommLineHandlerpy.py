from StringParser import StringParser
from TestConfig import TestConfig
from TestComplete import TestComplete
from CustomException import CustomException
from Login import Login

class ParameterType():
  def Environment(paramVal):
      TestConfig.Environment = paramVal
      Log.Message("The 'Environment' argument is found! The value is '" + paramVal + "'")
      if TestConfig.Environment != "PROD":
          TestConfig.IsProd = 0

  def TestBrowser(paramVal):
      TestComplete.TestBrowser = paramVal
      Log.Message("The 'TESTBROWSER' argument is found! The value is '" + paramVal + "'")

  def Suitetorun(paramVal):
      TestConfig.SuiteToRun = paramVal
      Log.Message("The 'SUITETORUN' argument is found! The value is '" + paramVal + "'")
      if TestConfig.SuiteToRun == "MDBPRODMONITOR":
          TestConfig.IsProd = 0
          
  def SetApplicationUrl(paramVal):
      TestComplete.AppURL = paramVal
      TestConfig.URL = paramVal
      Log.Message("The 'APPURL' argument is found! The value is '" + paramVal + "'")
      
  def SetUserName(paramVal):
      Login.UserName = paramVal
      Log.Message("The 'USERNAME' argument is found! The value is '" + paramVal + "'")
      
  def SetPassword(paramVal):
      Login.Password = paramVal
      Log.Message("The 'PASSWORD' argument is found! The value is '" + paramVal + "'")
          
  def Setkycqa(paramVal):
      Login.kycqa = paramVal
      Log.Message("The 'KYCQA' argument is found! The value is '" + paramVal + "'")
      
  def SetkycqaPassword(paramVal):
      Login.Passwordkycqa = paramVal
      Log.Message("The 'PASSWORDKYCQA' argument is found! The value is '" + paramVal + "'")
      
  def Setkycqa2(paramVal):
      Login.kycqa2 = paramVal
      Log.Message("The 'KYCQA2' argument is found! The value is '" + paramVal + "'")
      
  def Setkycqa2Password(paramVal):
      Login.Passwordkycqa2 = paramVal
      Log.Message("The 'PASSWORDKYCQA2' argument is found! The value is '" + paramVal + "'")
  
  def SetIsRenameFile(paramVal):
      TestConfig.IsRenameFile = paramVal
      Log.Message("The 'ISRENAMEFILE' argument is found! The value is '" + paramVal + "'")
      
class CommLineHandler():
  paramcases = {
    "environment" : ParameterType.Environment ,
    "testbrowser" : ParameterType.TestBrowser ,
    "suitetorun"  : ParameterType.Suitetorun,
    "appurl"      : ParameterType.SetApplicationUrl,
    "username"    : ParameterType.SetUserName,
    "password"    : ParameterType.SetPassword,
		"insightanalystuser": ParameterType.Setkycqa,
		"insightanalystuserpass": ParameterType.SetkycqaPassword,
		"insightmanuser": ParameterType.Setkycqa2,
		"insightmanpass": ParameterType.Setkycqa2Password,
		"isrenamefile"  : ParameterType.SetIsRenameFile
  }
  
  def ParamSwitch(paramcases, args ):
    Log.Message(str(args))
    param = StringParser.remAllWhiteSpaces(StringParser.toLower(args[0]))
    paramVal = StringParser.remAllWhiteSpaces(args[1])
    return paramcases[ param ]( paramVal )
  
  def ProcessCommandLine(self):
    Log.Message(int(BuiltIn.ParamCount()))
    for i in range (1, int(BuiltIn.ParamCount())):
      commLineParam = BuiltIn.ParamStr(i)
      Log.Message("Command Line Parameters :: " + commLineParam)
      CommLineHandler.ProcessCommandLineArgument(commLineParam)
    
  def testCommandLine():
    str = "ENVIRONMENT=QA;;TESTBROWSER=iexplore;;SUITETORUN=MDBFULLREG"
    CommlineHandler.ProcessCommandLineArgument(str)
    
  def ProcessCommandLineArgument(arg):
    argsList = StringParser.splitStr(arg,";;")
    if not len(argsList):
      raise CustomException("Test Suite Command Line arguments missing")
    for arg in argsList:
      CommLineHandler.ProcessArgs(arg)
  
  def ProcessArgs(commparam):
    argsList = StringParser.splitStr(commparam,"=")
    #Log.Message("CommParam = " + commparam + " and number of args: = " + str(len(argsList)))
    if len(argsList)> 1:
      CommLineHandler.ParamSwitch(CommLineHandler.paramcases,argsList)
