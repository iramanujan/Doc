class TestConfig:
    TempLocation = Project.Path+"TestRepo\\TempFiles";
    TestSuiteName = ""
    TestSuiteID = ""
    ChildCount = ""
    TestCaseId = ""
    TestCaseName = ""
    TestCaseSteps = ""
    Parameter1 = ""
    Parameter2 = ""
    Execution_Id = ""
    SummaryID = ""
    DetailID = ""
    Environment = ""
    SuiteToRun = ""
    IsIgnore = "N"
    ObjRepName = ""
    DownloadFilePath = ""
    SuiteType = ""
    StopSuite = ""
    URL = None
    InputFilePath = ""
    IsRenameFile = 1
    
    TempDict = {}
    
    def __init__(self):
        Log.Message("Initializing TestConfig Class");
        
    def SetValeInTempDict(Key,Value):
      Log.Message("Key :{'" + Key +"'}; Value: {'"+str(Value)+"'}")
      TestConfig.TempDict[Key] = str(Value)
    
    def GetValeFromTempDict(Key):
      Log.Message(TestConfig.TempDict[Key])
      return TestConfig.TempDict[Key];
      
    