echo ******************************Restoring SQL DB *************************
taskkill /F /IM CXSRetailPOS.exe
taskkill /F /IM CXSManagementConsole.exe
sqlcmd -S %computername%\SQLEXPRESS  -U sa -P Passw0rd  -i SqlDbUpdate.sql

echo ******************************SQL DB Restored *************************
Timeout 10