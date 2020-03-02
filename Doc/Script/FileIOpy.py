import os, datetime
from pathlib import Path
import shutil
import glob
from TCNameMapping import TCNameMapping
from StringParser import StringParser
from Helper import Helper
from TestComplete import TestComplete
from TestConfig import TestConfig
from distutils.dir_util import copy_tree
from LoggerHandler import LoggerHandler
class FileIO:
  
	def __init__(self):
		Log.Message("Initializing FileSystem handler Class");
	        
	def emptyDir(folder):
	  if not FileIO.exist(folder):
	    FileIO.createDir(folder)
	    return
	  for root, dirs, files in os.walk(folder):
	    for f in files:
	      os.unlink(os.path.join(root, f))
	    for d in dirs:
	      shutil.rmtree(os.path.join(root, d))
	  
	def delDir(folder):
	  shutil.rmtree(folder)
	
	def delFile(FilePath):
	  os.unlink(FilePath)

	def isDirEmpty(folder):
	  if os.path.exists(folder) and os.path.isdir(folder):
	    return(not os.listdir(folder))
	  else:
	    Log.Message("Directory: " + folder + " does not exist")
	    return False
	
	def exist(fileOrFolder):
	  return os.path.exists(fileOrFolder)
	  
	def createDir(folder):
	  import pathlib
	  pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
	
	def getFileList(folder):
	  (_, _, filenames) = next(os.walk(folder))
	  return filenames
	
	def searchFiles(folder,searcCri):
	  return glob.glob(os.path.join(folder, searcCri)) 
	
	def getLatestFile(folder):
	  list_of_files = glob.glob(os.path.join(folder, "*"))
	  return max(list_of_files, key=os.path.getctime)
	
	def getParentDir(filePath):
	  from pathlib import Path
	  return str(Path(filePath).parent)
	  
	def getFileNameFromPath(filePath):
	  return os.path.basename(filePath)
	  
	def getFileExtension(filePath):
	  Log.Message(filePath)
	  return os.path.splitext(str(filePath))[1]
	  
	def getFileBaseName(filePath):
	  return os.path.splitext(filePath)[0]
	  
	def renameFile(srcFilePath,destFilePath):
	  os.rename(srcFilePath, destFilePath)
	
	def copyFiles(src,dest):
	  import errno
	  try:
	    shutil.copytree(src,dest)
	  except OSError as e:
	    # If the error was caused because the source wasn't a directory
	    if e.errno == errno.ENOTDIR:
	      shutil.copy(src, dest)
	    else:
	      strVal = 'Directory not copied. Error: %s' % e
	      Log.Message(strVal)
	      
	def moveAllFiles(src,dest):
	  SrcFileList = FileIO.getFileList(src)
	  for sfile in SrcFileList:
	    copyPath = os.path.join(dest,sfile)
	    shutil.move(os.path.join(src,sfile),copyPath)
	    #FileIO.moveFile(os.path.join(parentDir,File),TestConfig.DownloadFilePath)
	    
	
	def moveFile(srcFilePath,destFilePath):
	  Log.Message(srcFilePath)
	  Log.Message(destFilePath)
	  name = ""
	  dirFlag = 0
	  if os.path.isdir(srcFilePath):
	    dirFlag = 1
	    if not FileIO.getFileList(srcFilePath):
	      Log.Warning("No Files to Move")
	      return
	    destParentFold = destFilePath
	    
	  else:
	    destParentFold = FileIO.getParentDir(destFilePath)
	    name =  FileIO.getFileNameFromPath(destFilePath)
	    	  
	  #if FileIO.getFileExtension(destFilePath):
	  #  destParentFold = FileIO.getParentDir(destFilePath)
	  #else:
	  #  destParentFold = destFilePath
	  if not FileIO.exist(destParentFold):
	    FileIO.createDir(destParentFold)
	  
	  if FileIO.exist(destFilePath) and dirFlag == 0:
	    Log.Message("FileMOVE: File already exists: " + destFilePath)
	    base, extension = os.path.splitext(name)
	    i = 1
	    while os.path.exists(os.path.join(destParentFold, '{}_{}{}'.format(base, i, extension))):
	      i += 1
	    npath = os.path.join(destParentFold, '{}_{}{}'.format(base, i, extension))
	    Log.Message("New Filename: " + npath)
	    shutil.move(srcFilePath,npath)
	  elif dirFlag == 0:
	    shutil.move(srcFilePath,destFilePath)
	  if dirFlag == 1:
	    FileIO.moveAllFiles(srcFilePath,destFilePath)
	    #shutil.move(srcFilePath,destFilePath)
  
	def unzipFile(FilePath,DestPath):
	  import zipfile
	  zip_ref = zipfile.ZipFile(FilePath, 'r')
	  zip_ref.extractall(DestPath)
	  zip_ref.close()
	  FileIO.delFile(FilePath)
	
	def unzipAll(FilePath,DestPath):
	  FileIO.unzipFile(FilePath,DestPath)
	  zipFileList = FileIO.searchFiles(DestPath,"*.zip")
	  if len(zipFileList)!=0:
	    for zipFile in zipFileList:
	      FileIO.unzipAll(zipFile,DestPath)

	def directDwn(DwnFolderPath):
	  dwnRes = False
	  StartTime = Helper.GetCurrentTime();
	  ElapsedTime = 0
	  while FileIO.isDirEmpty(DwnFolderPath):
	    if(ElapsedTime > 5):
	      Log.Error("Download Failed for File")
	      return dwnRes
	    if(TestComplete.TestBrowser == "iexplore"):
	      directUIHWNDlist = [TCNameMapping.IeDirectUIHWND,TCNameMapping.IeDwndirectUIHWND]
	      for dwnBr in directUIHWNDlist:
	        if dwnBr.Exists:
	          dwnBr.Focus()
	          if TCNameMapping.IeDirectUIHWNDSave.Exists:
	            TCNameMapping.IeDirectUIHWNDSave.click()
	          dwnBr.Keys("~S")
	          break
	    ElapsedTime = Helper.GetTimeDiffInMinutes(StartTime,Helper.GetCurrentTime())
	  
	  dwnFile = FileIO.getLatestFile(DwnFolderPath)
	  StartTime = Helper.GetCurrentTime();
	  while FileIO.getFileExtension(dwnFile)==".partial":
	    if(ElapsedTime > 4):
	      return dwnRes
	    dwnFile = FileIO.getLatestFile(DwnFolderPath)
	    ElapsedTime = Helper.GetTimeDiffInMinutes(StartTime,Helper.GetCurrentTime())
	  for dwnBr in directUIHWNDlist:
	    if dwnBr.Exists:
	      TCNameMapping.IeDirectUIHWNDClose.Click()
	  #unlock the downloaded file
	  powerShellComm = "dir " + DwnFolderPath + " -Recurse | Unblock-File"
	  Helper.execCLIComm("powershell -command " +powerShellComm)
	  
	def RenameFilesByRegex(FolderPath, RenameExpression, ReplaceBy):
	  fileList = FileIO.getFileList(FolderPath)
	  for file in fileList:
	    newFileBaseName = StringParser.regexReplace(RenameExpression,FileIO.getFileBaseName(file),ReplaceBy)
	    newFileName = newFileBaseName + FileIO.getFileExtension(file)
	    FileIO.renameFile(os.path.join(FolderPath,file),os.path.join(FolderPath,newFileName))
	
	def delFilesByRegex(FolderPath,Pattern):
	  for file in FileIO.getFileList(FolderPath):
	    if StringParser.TextContains(Pattern,FileIO.getFileBaseName(file)):
	        FileIO.delFile(os.path.join(FolderPath,file))
	  
	def moveDwnToTemp(ExpFileName):
	  parentDir = FileIO.getParentDir(ExpFileName)
	  if(parentDir=="."):
	    parentDir = os.path.join(os.environ['USERPROFILE'],"Downloads")
	  #Move this temp location D:\loggedinuser_temp\ folder
	  aqUtils.Delay(3000,"some extra wait before moving files")
	  DwnFileList = FileIO.getFileList(parentDir)
	  if len(DwnFileList)>1:
	    import tempfile
	    destDir = os.path.join("D:\\", os.getlogin() + "_autoTemp")
	    with tempfile.TemporaryDirectory() as destDir:
	      Log.Message("created temporary directory" + destDir)
	      extrFolder = os.path.join(destDir,ExpFileName)
	      FileIO.createDir(extrFolder)
	      for dwnFile in DwnFileList:
	        #if it is a zip file - unpack it
	        dwnFileExt = FileIO.getFileExtension(dwnFile)
	        if dwnFileExt == ".zip":
	          FileIO.unzipAll(os.path.join(parentDir,dwnFile),extrFolder)
	        else:
	          tempPath = os.path.join(destDir,dwnFile)
	          FileIO.moveFile(os.path.join(parentDir,dwnFile),tempPath)
	      if TestConfig.IsRenameFile == 1:
	        FileIO.delFilesByRegex(extrFolder,"^(?!Consolidated Stmnt).*")
	        FileIO.RenameFilesByRegex(extrFolder,r"-\d.*$","")
	      FileIO.moveFile(extrFolder,TestConfig.TempLocation + "\\")
	  else:
	      dwnFile = FileIO.getFileList(parentDir)
	      for File in dwnFile:
	        dwnFileExt = FileIO.getFileExtension(File)
	        newFileName = FileIO.getFileBaseName(ExpFileName) + dwnFileExt
	        TestConfig.DownloadFilePath = os.path.join(TestConfig.TempLocation,newFileName)
	        FileIO.moveFile(os.path.join(parentDir,File),TestConfig.DownloadFilePath)
	        
	def WriteTextIntoFile(FileLocation,Data):
	  FilePath = Path(FileLocation)
	  if(FilePath.is_file()):
	    File = open(FilePath,"a");
	  else:
	    File = open(FilePath,"w");
	  File.write(Data+"\n")
	  File.close()
	    
	def GetAllSubFolderList(RootDir):
		SubDirList = list();
		for dirName, subdirList, fileList in os.walk(RootDir):
			if(dirName != RootDir):
				SubDirList.append(dirName)
				
	def IsFileExist(FileLocation):
	  FilePath = Path(FileLocation)
	  return FilePath.is_file();

	def CopyFileAndFolder():
	  SourceLocation = Project.Path+Helper.ReadConfig().get("SourceLocation")
	  DestinationLocation   =    Project.Path+Helper.ReadConfig().get("DestinationLocation")
	  Log.Message(SourceLocation)
	  Log.Message(DestinationLocation)
	  DestinationDir = os.path.join(DestinationLocation, 'ReportExport_'+datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S'))
	  LoggerHandler.LogInfo("Pass",TestCaseSteps = "Move All File and Folder",CustomMessage="From Location and To Location",Parameter1="Destination Location: "+DestinationDir,Parameter2="Source Location: "+SourceLocation)
	  os.makedirs(DestinationDir)
	  copy_tree(SourceLocation,DestinationDir)