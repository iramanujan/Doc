echo Running Regression For Citixsys

taskkill /F /IM TestExecute.exe
taskkill /F /IM TestComplete.exe
taskkill /F /IM Excel.exe
set failedLogsPath=C:\temp\FailedTestItemsLogs
del c:\temp\RegressionResult.csv
del /Q %failedLogsPath%
mkdir %failedLogsPath%
TIMEOUT 10

set year=%date:~10,4%
set month=%date:~4,2%
set day=%date:~7,2%
echo data is %date%
set dateTimeYr=%year%_%month%_%day%

set timedata=%time:~0,2%_%time:~3,2%_%time:~6,2%

set FolderPath=D:\CitiXsysRegressionData\
mkdir %FolderPath%
set GitPath=%FolderPath%Git_%date%_%timedata%
set GitPath=%GitPath: =_%
set GitPath=%GitPath:/=_%
mkdir %GitPath%
set LogPath=D:\RegressionLogs\%date%\
set LogPath=%LogPath: =_%
set LogPath=%LogPath:/=_%
mkdir %LogPath%

set branchName=Anuj
set LogFileName=RegressionLog_%date%_%timedata%
set ProjectPath=%GitPath%\CitiXsysAutomation\
set ProjectFile=%ProjectPath%Citixsys_Automation_Suite.pjs
set ProjectName=Citixsys_Regression
set MhtLogFilePath=%LogPath%HtmlLogs\%LogFileName%.mht

set MhtLogFilePath=%MhtLogFilePath: =_%
set MhtLogFilePath=%MhtLogFilePath:/=_%
REM get the git repository
set existingDir=%cd%

REM Get git repository
echo Running Regression For Citixsys
git clone https://CXS-Projects@dev.azure.com/CXS-Projects/iVend.Automation/_git/iVend.Automation "%GitPath%"
TImeout 10
cd /D "%GitPath%"
TImeout 5
git checkout %branchName%
TImeout 5
git pull
TImeout 5
echo Git is cloned and checked Out
TImeout 5
REM call GitRepoCreate %GitPath% %branchName%
echo Git is cloned from other batch file at %GitPath% with branch %branchName%
Timeout 10

"C:\Program Files (x86)\SmartBear\TestComplete 14\x64\Bin\TestComplete.exe" "%ProjectFile%" /run /project:"%ProjectName%"  /exit /SilentMode /ForceConversion
REM "C:\Program Files (x86)\SmartBear\TestExecute 14\x64\Bin\TestExecute.exe" "%ProjectFile%" /run /project:"%ProjectName%" /ExportLog:"%MhtLogFilePath%" /exit /SilentMode /ForceConversion
echo Execution Completed
taskkill /F /IM TestExecute.exe
taskkill /F /IM TestComplete.exe
TIMEOUT 20
echo Sending Results via Email
cd /D "%existingDir%/"
C:\Users\anujjain03\AppData\Local\Programs\Python\Python37-32\python.exe SendEmail.py %MhtLogFilePath% %LogPath%
TIMEOUT 50
echo Regression Completed
copy /Y %failedLogsPath% %LogPath%
exit


echo Re-Running Regression For Citixsys
set MdsFilePath=%GitPath%\CitiXsysAutomation\Citixsys_Regression\Citixsys_Regression.mds
set CsvFilePath=c:\temp\RegressionResult.csv
C:\Users\anujjain03\AppData\Local\Programs\Python\Python37-32\python.exe  ReRun.py %CsvFilePath% %MdsFilePath%
taskkill /F /IM TestExecute.exe
taskkill /F /IM TestComplete.exe
taskkill /F /IM Excel.exe
set failedLogsPath=C:\temp\FailedTestItemsLogs
del c:\temp\RegressionResult.csv
del /Q %failedLogsPath%
mkdir %failedLogsPath%
TIMEOUT 10