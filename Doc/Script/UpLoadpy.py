import os
from TestComplete import TestComplete
from LoggerHandler import LoggerHandler
from TestConfig import TestConfig
from TCNameMapping import TCNameMapping
from UDF import UDF

class UpLoad:
  FileMapping = {};
  def __init__(self):
    self.FileMapping ={
        "ECR-Dmod.dmod":"TestRepo\\TestSuite\\UploadFile\\ECR-Dmod.dmod",
        "ECR-Sample.csv":"TestRepo\\TestSuite\\UploadFile\\ECR-Sample.csv",
        "ECR-Txt.txt":"TestRepo\\TestSuite\\UploadFile\\ECR-Txt.txt",
        "ECR-XML.xml":"TestRepo\\TestSuite\\UploadFile\\ECR-XML.xml",
        "Sample.pdf":"TestRepo\\TestSuite\\UploadFile\\Sample.pdf",
        "sample.xlsx":"TestRepo\\TestSuite\\UploadFile\\sample.xlsx",
        "Samplenotepad.txt":"TestRepo\\TestSuite\\UploadFile\\Samplenotepad.txt"
    }
		

  def UpLoadFile(self,FileName):
    #RootDir = Project.Path+"TestRepo\\TestSuite\\UploadFile"
    RootDir = TestConfig.InputFilePath + "\\UploadFile"
    for root, dirnames, filenames in os.walk(RootDir):
      for File in filenames:
        if(File == FileName):
          return os.path.join(root, File)
          
  def UpLoad(self,PropertyList,FileName):
    FilePath = UpLoad.UpLoadFile(self,FileName)
    ObjUdf = UDF();
    ObjUdf.OpenFile(FilePath)
#    FilenameEditBox = None
#    ButtonOpen = None 
#    OpenFileDialog = None
#    if(TestComplete.TestBrowser == "chrome"):
#      OpenFileDialog      =   TCNameMapping.GCOpenFileDialog
#      FilenameEditBox     =   TCNameMapping.GCFilenameEditBox
#      OpenFileDialog      =   TCNameMapping.GCButtonOpen
#    if(TestComplete.TestBrowser == "iexplore"):
#      OpenFileDialog      =   TCNameMapping.IEOpenFileDialog
#      FilenameEditBox     =   TCNameMapping.IEFilenameEditBox
#      OpenFileDialog      =   TCNameMapping.IEButtonOpen
#    
#    Counter = 0  
#    while(not OpenFileDialog.Exists):
#      if(int(Counter) > 60):
#        ErrMessage = OpenFileDialog.WndCaption + " not found. Uploading Failed for File: " + FilePath
#        TestConfig.IsIgnore = "Y"
#        LoggerHandler.LogInfo("Failed",CustomMessage=ErrMessage,Parameter1=FilePath)
#        return
#      aqUtils.Delay(1000,"Waiting For " + OpenFileDialog.WndCaption + " Dialog");
#      Counter =  Counter + 1
#      
#    if(OpenFileDialog.Exists):
#      FilenameEditBox.Click(98, 6)
#      FilenameEditBox.SetText("")
#      FilenameEditBox.SetText(FilePath)
#      OpenFileDialog.ClickButton()
#    else:
#      ErrMessage = OpenFileDialog.WndCaption + " not found. Uploading Failed for File: " + FilePath
#      TestConfig.IsIgnore = "Y"
#      LoggerHandler.LogInfo("Failed",CustomMessage=ErrMessage,Parameter1=FilePath)
#      return