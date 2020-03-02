REM set ProjectFile=D:\CitiXsysRegressionData\Git_Mon_04_22_2019_19_01_32\CitiXsysAutomation\Citixsys_Automation_Suite.pjs
REM set ProjectName=Citixsys_Regression
REM set MhtLogFilePath=D:\testLogs\MHT.tcLogX
REM "C:\Program Files (x86)\SmartBear\TestComplete 12\x64\Bin\TestComplete.exe" "%ProjectFile%" /run /project:"%ProjectName%" /ExportLog:"%MhtLogFilePath%" /exit /SilentMode

python SendEmail.py dd dd

Timeout 100
