import site
site.addsitedir(Project.Path+"TestRepo\\PyPackages")
import sys
import pyodbc
from TestConfig import TestConfig
from Helper import Helper
import os, datetime
import pandas as pd

class DBConnector:
  Connection = None;
  
  def __init__(self):
    Log.Message("Initializing DBConnector Class");
      
  def GetConnection(self,ServerName,DatabaseName,UserName = None,Password = None):
    Log.Message("Initializing Database Connector");
    if(UserName is None and Password is None):
      Connection  = pyodbc.connect("Driver={SQL Server};Server="+ServerName+";Database="+DatabaseName+";Trusted_Connection=yes;")
    else:
      Connection =  pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server};Server="+ServerName+";Database="+DatabaseName+";UID="+UserName+";PWD="+ Password)
      #Connection  = pyodbc.connect("Driver={SQL Server};Server="+ServerName+";Database="+DatabaseName+";Trusted_Connection=yes;")
    return Connection;
      
  def GetDBValue(self,SQLCommand,ServarName,DataBaseName,UserId=None,Password=None):
    ResultList = self.SelectCommand(SQLCommand,ServarName,DataBaseName,UserId,Password)
    return ResultList
    
  def SelectCommand(self,SQLCommand,ServarName,DataBaseName,UserId=None,Password=None):
    ResultList = list();
    try:
      Connection = self.GetConnection(ServarName,DataBaseName,UserId,Password)
      cursor = Connection.cursor()
      cursor.execute(SQLCommand)
      results = cursor.fetchone()
      ResultList = list();
      Log.Message("SQL Command: "+SQLCommand)
      while results:
        ResultList.append(list(results))
        results = cursor.fetchone()
      Log.Message(str(ResultList))  
      return ResultList
    except Exception as E:
      tb = sys.exc_info()[2]
      Log.Message(str(E.with_traceback(tb)))
    finally:
      cursor.close();
      del cursor
      Connection.close()
      
  def DatabaseToExcel(self,PropertyList,ProcName,FileName):
    from FileIO import  FileIO
    DestinationDir   =    Project.Path+Helper.ReadConfig().get("SourceLocation")
    FileIO.createDir(DestinationDir)
    ServerName = Helper.ReadConfig().get("NetikSrvName")
    DatabaseName = Helper.ReadConfig().get("NetikDbName")
    Connection = self.GetConnection(ServerName,DatabaseName,None,None)
    StoredProceduresName = "{"+ProcName.split(";")[1].replace('EXEC', 'Call')+"}"
    DataSet = pd.read_sql(sql=StoredProceduresName, con=Connection)
    DataHeaderList = list(DataSet)
    for Header in DataHeaderList:
      DataSet[Header] = DataSet[Header].astype(str)
    FilePath = DestinationDir+"\\"+FileName+".xlsx"
    DataSet.to_excel(FilePath,sheet_name = FileName,index = False)
    
  def InsertCommand(self,SQLCommand,ServarName,DataBaseName,UserId=None,Password=None):
    try:
      Connection = self.GetConnection(ServarName,DataBaseName,UserId,Password)
      cursor = Connection.cursor()
      cursor.execute(SQLCommand)
      cursor.commit()
    except Exception as E:
      tb = sys.exc_info()[2]
      Log.Message(SQLCommand)
      Log.Message(str(E.with_traceback(tb)))
    finally:
      cursor.close();
      del cursor
      Connection.close()
      
  def RunSql(self,ParamList,SqlCommand):
    ServerName = Helper.ReadConfig().get("NetikSrvName")
    DatabaseName = Helper.ReadConfig().get("NetikDbName")
    ObjDBConnector = DBConnector();
    ObjDBConnector.InsertCommand(SqlCommand,ServerName,DatabaseName,None,None)