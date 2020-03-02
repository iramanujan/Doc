def GeneralEvents_OnStopTest(Sender):
    Log.Message("Stop Event Captured")
    from TestConfig import TestConfig
    TestConfig.StopSuite = "Y"
    from LoggerHandler import LoggerHandler
    LoggerHandler.UpdateAutomationExecution("Completed with Errors")
    #raise Exception("Stopping Suite Execution")
    #Runner.Stop()