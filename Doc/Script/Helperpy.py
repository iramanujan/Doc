from ConfigReader import ConfigReader
import datetime
from random import *
import decimal
import string
import subprocess
from TCNameMapping import TCNameMapping
import os


class Helper:

	def __init__(self):
		Log.Message("Initializing Helper Class")

	def execCLIComm(Comm):
	  subprocess.call(Comm)
	
	def closeAllBrowser():
		Helper.execCLIComm("cmd /c TASKKILL /F /IM firefox.exe /T")
		Helper.execCLIComm("cmd /c TASKKILL /F /IM chrome.exe /T")
		Helper.execCLIComm("cmd /c TASKKILL /F /IM iexplore.exe /T")
		#Helper.execCLIComm("cmd /c TASKKILL /F /IM Excel.exe /T")

	  
	def CloseProcess(AppName):
	  ObjSys = Sys.WaitProcess(AppName,100)
	  if(ObjSys.Exists):
	    ObjSys.Close()
	    if(ObjSys.Exists):
	      Log.Warning(AppName + " was not closed successfully and will be terminated.")
	      ObjSys.Terminate()
	    
  
	def GetRandomEmail(Range):
	  aqString.ListSeparator = "-"
	  min = aqConvert.StrToInt(aqString.GetListItem(Range,0))
	  max = aqConvert.StrToInt(aqString.GetListItem(Range,1))
	  RandomText = "".join(choice(string.ascii_letters) for x in range(randint(min,max)))
	  RandomText = RandomText + "@seic.com" 
	  return RandomText
    
	def GetRandomText(Range):
	  aqString.ListSeparator = "-"
	  min = aqConvert.StrToInt(aqString.GetListItem(Range,0))
	  max = aqConvert.StrToInt(aqString.GetListItem(Range,1))
	  return "".join(choice(string.ascii_letters + string.digits) for x in range(randint(min,max)));
	  #return "".join(choice(string.ascii_letters + string.punctuation + string.digits) for x in range(randint(min,max)));
  
	def GetRandomInt(Range):
	  aqString.ListSeparator = "-"
	  min = aqConvert.StrToInt(aqString.GetListItem(Range,0))
	  max = aqConvert.StrToInt(aqString.GetListItem(Range,1))
	  return randint(min,max)
  
	def GetText():
	  return str("".join(choice(string.ascii_letters) for x in range(randint(10,15))));
	  
	def GetInt(InputType):
	  if(InputType == "VALID"):   return randint(9999,999999)
	  if(InputType == "INVALID"): return "".join(choice(string.ascii_letters) for x in range(randint(7,12)));
	  
	def GetDate(InputType):
	  if(InputType == "VALID"):
	    date = aqString.SubString(aqConvert.StrToDate(aqDateTime.Now()),0,10)
	    mm = date.split("/")[0]
	    dd = date.split("/")[1]
	    yy = date.split("/")[2]
	    return (mm+"/"+dd+"/"+yy)
	  if(InputType == "INVALID"): return "".join(choice(string.ascii_letters) for x in range(randint(7,12)));
	  
	def GetDecimal(InputType):
	  if(InputType == "VALID"):   return float(decimal.Decimal(randint(9999,999999))/100)
	  if(InputType == "INVALID"): return "".join(choice(string.ascii_letters) for x in range(randint(7,12)));
    
	def GetCurrentTime():
		return datetime.datetime.now().replace(microsecond=0);
		
	def GetTimeDiffInSecond(StartTime,EndTime):
	  return (EndTime-StartTime).total_seconds()
	  
	def GetTimeDiffInMinutes(StartTime,EndTime):
	  return ((EndTime-StartTime).total_seconds()/60);
	  
	def RemoveSpaces(InputText):
	  return aqString.Replace(aqString.Trim(InputText)," ","")
	  
	def ReadConfig():
	  myConfigReader = ConfigReader()
	  dictObj = myConfigReader.load_properties(myConfigReader.configFilePath)
	  #for keys,values in dictObj.items():
	    #Log.Message(keys+":"+values)
	  return dictObj
	
	def DwnSaveAsFile(DwnFolderPath):
	  saveAsDialog = TCNameMapping.SaveAsDialog
	  fileNameEditBox = TCNameMapping.SaveAsFileNameEditBox
	  saveAsBtn = TCNameMapping.SaveAsSaveBtn
	  #UnComment this function if required
	  #Waiting for saveAsDialog to popup
	  #PropertyList = ["NAMEMAPPING",saveAsDialog]
	  #WebObjectHandler.WaitForObject(PropertyList,1)
	  #fileNameEditBox.Click(98,6)
	  #fileNameEditBox.setText("")
	  #fileNameEditBox.SetText(DwnFolderPath + "\\")
      #saveAsBtn.ClickButton
	  
	def GetHostName():
	  return os.getenv('COMPUTERNAME')
	  
	def GetLoginUser():
	  return os.getlogin();
	
	def GetFCurrTimeHMS():
	  now = datetime.datetime.now()
	  return str(now.strftime("%I:%M:%S"))
	  
	def IsDate(date):
		if(date == None or date == "NULL"): return False
		elif(not(date and date.strip())): return False
    
		mm,dd,yy = date.split('/')
		dd = int(dd)
		mm = int(mm)
		yy = int(yy)    
    
		if(mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
		    max1 = 31
		elif(mm == 4 or mm == 6 or mm == 9 or mm == 11):
		    max1 = 30
		elif(yy % 4 == 0 and yy % 100 != 0 or yy % 400 == 0):
		    max1 = 29
		else:
		    max1 = 28
		if(mm < 1 or mm > 12):
		    return False
		elif(dd < 1 or dd > max1):
		    return False
		elif(yy <= 0):
		    return False
		else:
		    return True
	
	def DiffList(li1, li2):
	  return list(set(li1) - set(li2))
	  
	def CompList(li1,li2):
	  diff = Helper.DiffList(li1,li2)
	  return not(len(diff))
	def GetRandInput(FieldType,InputType,OrignalValue):
	  RandVal = None;
	  if(aqString.ToUpper(FieldType) == "TEXT"):
	    RandVal = Helper.GetText();
	    if(RandVal == OrignalValue):
	      RandVal = Helper.GetText();
	  if(aqString.ToUpper(FieldType) == "NUMBER"):
	    RandVal = Helper.GetInt(InputType);
	    if(RandVal == OrignalValue):
	      RandVal = Helper.GetInt(InputType);
	  if(aqString.ToUpper(FieldType) == "DATE"):
	    RandVal = Helper.GetDate(InputType);
	    if(RandVal == OrignalValue):
	      RandVal = Helper.GetDate(InputType);
	  if(aqString.ToUpper(FieldType) == "DECIMAL"):
	    RandVal = Helper.GetDecimal(InputType);
	    if(RandVal == OrignalValue):
	      RandVal = Helper.GetDecimal(InputType);
	  return RandVal;