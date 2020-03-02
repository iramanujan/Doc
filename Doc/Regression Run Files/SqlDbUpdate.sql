use master
alter database CXSRetail_PKDB set single_user with rollback immediate
drop database CXSRetail_PKDB

RESTORE DATABASE CXSRetail_PKDB  
   FROM DISK = 'C:\Program Files\Microsoft SQL Server\MSSQL12.SQLEXPRESS\MSSQL\Backup\CXSRetail_PKDB.bak' ; 

alter database CXSRetail_PKDB set MULTI_USER
