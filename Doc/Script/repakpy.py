from LoggerHandler import LoggerHandler
from WebObject import WebObject
from WebObjectHandler import WebObjectHandler
from TestComplete import TestComplete
from FileIO import FileIO
from StringParser import StringParser
from Helper import Helper
from Login import Login
from TestConfig import TestConfig
import os
from pathlib import Path
import shutil
import glob
import site
from Action import Action as RepAct
from ExcelDriver import ExcelDriver

class ReportPackage:
  RepPackageId = ""
  RepPackageName = ""
  ExportFileName = ""
  DwnExpFileName = ""
  
  def __init__(self):
    Log.Message("Initializing ReportPackage Class")
  
  def getReportPackageId(webelement):
    ReportPackage.RepPackageId = webelement.textContent
    LoggerHandler.LogInfo("Info",CustomMessage="Report Package Id Stored As",Parameter1=ReportPackage.RepPackageId)
  
  def getReportPackageName(webelement):
    ReportPackage.RepPackageName = webelement.value
    LoggerHandler.LogInfo("Info",CustomMessage="Report Package Name Stored As",Parameter1=ReportPackage.RepPackageName)
    
  def getRepExportFileName(webelement):
    ReportPackage.ExportFileName = webelement.value
    LoggerHandler.LogInfo("Info",CustomMessage="Report Package Exported File Name Stored As",Parameter1=ReportPackage.ExportFileName)

  def VerifySearchAvailableList(self,PropList,RepInqNum):
    act = RepAct()
    tempSelector = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("SelectListRepNumberGeneric"),"REPINQ",str(RepInqNum))
    RowRepNumAvailList = act.GetObject(tempSelector)
    if(RowRepNumAvailList is not None and RowRepNumAvailList.textContent == RepInqNum):
      LoggerHandler.LogInfo("Pass",CustomMessage="Available List Search successful for Report",Parameter1=RepInqNum)
    else:
      Log.Warning("Available List Search failed for Report: "+ RepInqNum,"", pmHighest, None, Sys.Desktop)
      LoggerHandler.LogInfo("Failed",CustomMessage="Available List Search failed for Report",Parameter1=RepInqNum)

  def VerifySearchSelList(self,PropList,RepIdentifier):
    act = RepAct()
    firstRowRepNumSelList = act.GetObject(WebObject.getPropertyList("SelectListFirstRowRepNumber"))
    if(firstRowRepNumSelList is not None and firstRowRepNumSelList.textContent == RepIdentifier):
      LoggerHandler.LogInfo("Info",CustomMessage="REPINQ of first record in selected list",Parameter1=firstRowRepNumSelList.textContent)
      LoggerHandler.LogInfo("Pass",CustomMessage="Selected List Search successful for Report",Parameter1=RepIdentifier)
    else:
      Log.Warning("Selected List Search failed for Report: "+ RepIdentifier,"", pmHighest, None, Sys.Desktop)
      LoggerHandler.LogInfo("Failed",CustomMessage="Selected List Search failed for Report",Parameter1=RepIdentifier)
    
  def VerifySchedPackageLabel():
    act = RepAct()
    RepPackLabel = act.GetObject(WebObject.getPropertyList("SchedPackRepPackLabel"))
    if(RepPackLabel is not None and RepPackLabel.textContent == ReportPackage.RepPackageName):
      LoggerHandler.LogInfo("Pass",CustomMessage="Schedule Screen report package label matches",Parameter1=ReportPackage.RepPackageName)
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="Schedule Screen report package label does not match",Parameter1=ReportPackage.RepPackageName)

  def VerifySchedPackageJobName():
    act = RepAct()
    SchedPackJobName = act.GetObject(WebObject.getPropertyList("SchedPackSchedName"))
    if(SchedPackJobName is not None and SchedPackJobName.value == ReportPackage.RepPackageName):
      LoggerHandler.LogInfo("Pass",CustomMessage="Schedule job name matches with Rep Package name",Parameter1=ReportPackage.RepPackageName)
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="Schedule job name: " + SchedPackJobName.value + " <> Rep Package name:",Parameter1=ReportPackage.RepPackageName)

  def SelectReportByINQ(self,PropList,repInqNum):
    ObjAction = RepAct()
    ObjAction.ListItem(WebObject.getPropertyList("SelectListNumOfRecDropDwn"),"200")
    tempSelector = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("SelectListGenericCheckbox"),"REPINQ",str(repInqNum))
    Log.Message("Trying to look select checkbox for" + str(tempSelector))
    ObjAction.Click(tempSelector)

  
  def SearchForReportPackage(self,PropList,searchCriteria):
    ReportPackage.RepPackageName = TestConfig.GetValeFromTempDict("GETREPPACKAGENAME")
    ReportPackage.ExportFileName = TestConfig.GetValeFromTempDict("GETEXPORTFILENAME")
    if searchCriteria == "ByName":
      searchString = ReportPackage.RepPackageName
    elif searchCriteria == "ByRepPackID":
      ReportPackage.RepPackageId = TestConfig.GetValeFromTempDict("GETREPPACKAGEID")
      searchString = ReportPackage.RepPackageId
    Log.Message("Going to Type Search String: " + searchString)
    ObjAction = RepAct()
    ObjAction.ObjectKeyIn(WebObject.getPropertyList("RepPackageSearchBox"),searchString)
    TestComplete.hardWait(3000,"Searching for the Report Package")
    
  
  def VerifyRepPackGridSearch(self,PropList,searchCriteria):
    ObjAction = RepAct()
    firstRow = ObjAction.Sync(WebObject.getPropertyList("FirstRowRepPackId"))
    if(firstRow is not None):
      if searchCriteria == "ByName":
        LoggerHandler.LogInfo("Pass",CustomMessage="Search For Report Package " +  searchCriteria,Parameter1=ReportPackage.RepPackageName)
      elif searchCriteria == "ByRepPackID":
        LoggerHandler.LogInfo("Pass",CustomMessage="Search For Report Package " +  searchCriteria,Parameter1=ReportPackage.RepPackageId)
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="Search For Report Package " +  searchCriteria + " Failed")
    
  def VerRepPackGridAftDel():
    ObjAction = RepAct()
    ObjAction.ObjectKeyIn(WebObject.getPropertyList("RepPackageSearchBox"),ReportPackage.RepPackageId)
    TestComplete.hardWait(3000,"Wait for Rep package grid to load the rep package searched by id")
    firstRow = ObjAction.GetObject(WebObject.getPropertyList("FirstRowRepPackId"))
    if(firstRow is None):
      LoggerHandler.LogInfo("Pass",CustomMessage="Report Package Not found in grid",Parameter1=ReportPackage.RepPackageId)
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="Report Package found in grid",Parameter1=ReportPackage.RepPackageId)

  def VerRepPackLeftNavAftDel():
    Log.Message("Click to open left navigation bar")
    ObjAction = RepAct()
    ObjAction.Click(WebObject.getPropertyList("LeftNavOpenSearch"))
    ObjAction.Sync(WebObject.getPropertyList("LeftNavSearchField"))
    Log.Message("Search by Report package name on the left bar")
    ObjAction.ObjectKeyIn(WebObject.getPropertyList("LeftNavSearchField"),ReportPackage.RepPackageName)
    TestComplete.hardWait(3000,"Wait for left nav bar to search for rep package")
    tempSelector = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("RepLinkLeftNav"),"RPNAME",ReportPackage.RepPackageName)
    Log.Message("Trying to look for left nav link: " + str(tempSelector))
    LeftNavLink = ObjAction.GetObject(tempSelector)
    if(LeftNavLink is None):
      LoggerHandler.LogInfo("Pass",CustomMessage="Report Not Available in Left Nav After Delete",Parameter1=ReportPackage.RepPackageName)
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="Report Available in Left Nav After Delete",Parameter1=ReportPackage.RepPackageName)
    
  def VerifyDeleteRepPack():
    ReportPackage.VerRepPackGridAftDel()
    ReportPackage.VerRepPackLeftNavAftDel()
  
  def VerifyRepPackLeftNavSearch():
    ReportPackage.RepPackageId = TestConfig.GetValeFromTempDict("GETREPPACKAGEID")
    Log.Message("Click to open left navigation bar")
    ObjAction = RepAct()
    ObjAction.Click(WebObject.getPropertyList("LeftNavOpenSearch"))
    ObjAction.Sync(WebObject.getPropertyList("LeftNavSearchField"))
    Log.Message("Search by Report package name on the left bar")
    ObjAction.ObjectKeyIn(WebObject.getPropertyList("LeftNavSearchField"),ReportPackage.RepPackageName)
    TestComplete.hardWait(3000,"Wait for left nav bar to search for rep package")
    ObjAction.ObjectKeyIn(WebObject.getPropertyList("LeftNavSearchField"),ReportPackage.RepPackageName)
    LoggerHandler.LogInfo("Info",CustomMessage="Searching by report package name",Parameter1=ReportPackage.RepPackageName)
    tempSelector = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("RepLinkLeftNav"),"RPNAME",ReportPackage.RepPackageName)
    Log.Message("Trying to look for left nav link: " + str(tempSelector))
    LeftNavLink = ObjAction.Sync(tempSelector)
    if(LeftNavLink is not None):
      LoggerHandler.LogInfo("Pass",CustomMessage="Search For Report Package in Left Nav",Parameter1=ReportPackage.RepPackageName)
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="Search For Report Package in Left Nav",Parameter1=ReportPackage.RepPackageName)
      
    Log.Message("Click on Left nav link to open REport package Screen")
    ObjAction.Click(tempSelector)
    ObjAction.Sync(WebObject.getPropertyList("BtnNewPackage"))
    TestComplete.hardWait(4000,"Extra wait to let Report package screen open")
    
    Log.Message("Verify that on clicking left nav link, Report Package screen is opened with searched report package as default")
    repPackName = ObjAction.Sync(WebObject.getPropertyList("FirstRowRepPackName"))
    if (repPackName is not None) and (repPackName.textContent == ReportPackage.RepPackageName):
      LoggerHandler.LogInfo("Pass",CustomMessage="Grid is filtered on left nav click by name",Parameter1=ReportPackage.RepPackageName)
    else:
      Log.Warning("Grid is filtered on left nav click by name " + ReportPackage.RepPackageName,"", pmHighest, None, Sys.Desktop)
      LoggerHandler.LogInfo("Failed",CustomMessage="Grid is filtered on left nav click by name",Parameter1=ReportPackage.RepPackageName)
    
    repPackSearchBar = ObjAction.GetObject(WebObject.getPropertyList("RepPackageSearchBox"))
    if (repPackName is not None) and (repPackSearchBar.value == ReportPackage.RepPackageName):
      LoggerHandler.LogInfo("Pass",CustomMessage="Left Nav click - Report Package Search Bar is set to value",Parameter1=ReportPackage.RepPackageName)
    else:
      Log.Warning("Left Nav click - Report Package Search Bar is set to value " + ReportPackage.RepPackageName,"", pmHighest, None , Sys.Desktop)
      LoggerHandler.LogInfo("Failed",CustomMessage="Left Nav click - Report Package Search Bar is set to value",Parameter1=ReportPackage.RepPackageName)

  def downFile():
    DwnFolderPath = os.path.join(os.environ['USERPROFILE'],"Downloads")
    FileIO.emptyDir(DwnFolderPath)
    ObjAction = RepAct()
    RepAct.Download(DwnFolderPath)
    return FileIO.getLatestFile(DwnFolderPath)

  def VerifyRepPackExport(self,PropList,ExpType):
    ObjAction = RepAct()
    Log.Message("Click on ReportPackage Download Link to download the Report package")
    ObjAction.Click(PropList)
    dwnFileFullName = ReportPackage.downFile()
    ReportPackage.DwnExpFileName = dwnFileFullName
    Log.Message("Verify the name of file matches with the export file name")
    if ExpType == "CSVCONSOL":
      compString = ReportPackage.ExportFileName + ".csv"
    elif ExpType == "EXCELCONSOL":
      compString = ReportPackage.ExportFileName + ".xlsx"
    elif ExpType == "PDFCONSOL":
      compString = ReportPackage.ExportFileName + ".pdf"
    else:
      compString = ReportPackage.ExportFileName + ".zip"
    
    dwnFileName = FileIO.getFileNameFromPath(dwnFileFullName)
    if dwnFileName == compString:
      LoggerHandler.LogInfo("Pass",CustomMessage="Exported File has same name as File Name set by Rep Pack Wizard",Parameter1=dwnFileName)
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="Exported File name <> Rep Pack Wizard Export File name",Parameter1="Downloaded: " + dwnFileName, Parameter2="Expected: "+ compString)

  def OpenRp():
    refreshPage = 0
    ObjAction = RepAct()
    #WebObject.getPropertyList("LeftNavSearchField")
    Log.Enabled = False
    RPNewPackBtn = ObjAction.GetObject(WebObject.getPropertyList("BtnNewPackage"))
    if (RPNewPackBtn is not None):
      overLayDiv = ObjAction.GetObject(WebObject.getPropertyList("DivOverlay"))
      if (overLayDiv is not None):
        if StringParser.TextContains("display: none;",overLayDiv.style.CSSText) or overLayDiv.style.CSSText == "":
          return
        else:
          refreshPage = 1
      else:
        #refreshPage = 1
        return
    Log.Enabled = True
    if refreshPage == 1:
      #refresh the page
      TestComplete.refreshPage()
      TestComplete.hardWait(30000,"Waiting for page to reload after refresh")
      MDBMainPage = ObjAction.GetObject(WebObject.getPropertyList("EmtpyDashBoardImage"))
      if (MDBMainPage is not None):
        ReportPackage.OpenReportpackageScreen()
        return
    else:
      templogin = Login()
      templogin.IMSLogin()
      ReportPackage.OpenReportpackageScreen()
  
  def OpenReportpackageScreen():
    Log.Message("Click on Utilities Menu")
    ObjAction = RepAct()
    ObjAction.Click(WebObject.getPropertyList("MenuUtilities"))
    TestComplete.hardWait(3000,"Wait for Utilities menu to Populate")
    Log.Message("Wait for Utilities Menu to Populate")
    ObjAction.Click(WebObject.getPropertyList("OPENRP"))
    Log.Message("Wait For Report Package title to Appear")
    ObjAction.Sync(WebObject.getPropertyList("BtnNewPackage"))

  def VerifyExcelInclParamConsolidated(self,ParamList,ParamString):
    forStatus = 0
    result = "FAIL"
    #ReportPackage.DwnExpFileName    
    myExcelVar = ExcelDriver(ReportPackage.DwnExpFileName)
    #1 Asset Allocation Summary::Report Name: Asset Allocation Summary,,Report ID: 2766,,For: KAY E. TERKHORN : ExtAcct ID - 132392,,As Of: 6/30/2017,,Report Basis: Closed Period Investments;;1 Chart Asset Allocation Summar::Report Name: Asset Allocation Summary,,Report ID: 2766,,For: KAY E. TERKHORN : ExtAcct ID - 132392,,As Of: 6/30/2017,,Report Basis: Closed Period Investments;;2 Periodic Performance::Report Name: Periodic Performance,,Report ID: 17302,,For: Mesirow Small Cap Value Equity Composite : ExtAcct ID - AGGSEPMAN,,As Of: 9/30/2017,,Currency: USD;;3 Transaction Summary - Dynamic::Report Name: Transaction Summary - Dynamic YTD,,Report ID: 21360,,For: Doris A. Chernik PHD & Nina A. Chernik & Eric N. Chernik JT : ExtAcct ID - chernikd,,From: 4/1/2017,,To: 6/30/2017,,Date Type: Effective Posted Date,,Report Basis: Daily Investments;;3 Chart Transaction Summary - D::Report Name: Transaction Summary - Dynamic YTD,,Report ID: 21360,,For: Doris A. Chernik PHD & Nina A. Chernik & Eric N. Chernik JT : ExtAcct ID - chernikd,,From: 4/1/2017,,To: 6/30/2017,,Date Type: Effective Posted Date,,Report Basis: Daily Investments
    ParamSetList = StringParser.splitStr(ParamString, ";;")
    for ParamSet in ParamSetList:
      result = "FAIL"
      SheetName = StringParser.splitStr(ParamSet, "::")[0]
      RepParams = StringParser.splitStr(ParamSet,"::")[1]
      xlRec = myExcelVar.loadWorkSheetIntoMem(SheetName)
      if len(xlRec) < 1 :
        result = SheetName
        break
      firstColValList = [x[0] for x in xlRec]
      for cellVal in firstColValList:
        splitIndex = firstColValList.index(cellVal)
        splitArr = StringParser.splitStr(RepParams,",,")
        if splitIndex < len(splitArr):
          repParam = splitArr[splitIndex]
          if cellVal == repParam:
            Log.Message(cellVal + "=" + repParam)
            result = "PASS"
          else:
            Log.Message(cellVal + "<>" + repParam)
            result = SheetName
            forStatus = 1
            break
      if forStatus == 1:
        break
    if result == "PASS":
      LoggerHandler.LogInfo("Pass",CustomMessage="Parameters Included in Exported Excel for All reports")
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="Parameters Not Included in Exported Excel for report:",Parameter1="Expected: " + repParam,Parameter2="Actual: " + cellVal)
    
  def VerifyExcelInclParamUnConsolidated():
    Log.Message("VerifyExcelInclParamUnConsolidated")

  def VerifyExpExcelTabs(self,ParamList,ParamString):
    result = "FAIL"
    myExcelVar = ExcelDriver(ReportPackage.DwnExpFileName)
    sheetNameList = myExcelVar.getSheetNameList()
    expSheetList = StringParser.splitStr(ParamString,",")
    if Helper.CompList(sheetNameList,expSheetList):
      result = "PASS"
    if result == "PASS":
      LoggerHandler.LogInfo("Pass",CustomMessage="Consolidated Exported Excel has All Tabs")
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="Consolidated Exported Excel is mising tab",Parameter1=result)
    
  def VerifyExcelNoData(self,ParamList,ParamString):
    result = "FAIL"  
    myExcelVar = ExcelDriver(ReportPackage.DwnExpFileName)
    ParamSetList = StringParser.splitStr(ParamString, ";;")
    for ParamSet in ParamSetList:
      result = "FAIL"
      xlRec = myExcelVar.loadWorkSheetIntoMem(ParamSet)
      if len(xlRec) < 1 :
        result = SheetName
        break
      firstColValList = [x[0] for x in xlRec]
      for cellVal in firstColValList:
        if cellVal == "No Data Found":
          Log.Message(cellVal)
          result = "PASS"
          break
    if result == "PASS":
      LoggerHandler.LogInfo("Pass",CustomMessage="Consolidated Exported Excel has No Data for Tabs: ",Parameter1=ParamString)
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="Check for No Data found failed for sheet: ",Parameter1=result)
      
  def VerifyExcelInclExternalIdConsolidated(self,ParamList,ParamString):
    result = "FAIL"  
    myExcelVar = ExcelDriver(ReportPackage.DwnExpFileName)
    ParamSetList = StringParser.splitStr(ParamString, ";;")
    for ParamSet in ParamSetList:
      result = "FAIL"
      SheetName = StringParser.splitStr(ParamSet, "::")[0]
      RepParams = StringParser.splitStr(ParamSet,"::")[1]
      xlRec = myExcelVar.loadWorkSheetIntoMem(SheetName)
      if len(xlRec) < 1 :
        result = SheetName
        break
      firstColValList = [x[0] for x in xlRec]
      cellVal = firstColValList[3]
      if cellVal == RepParams:
        Log.Message(cellVal + "=" + RepParams)
        result = "PASS"
    if result == "PASS":
      LoggerHandler.LogInfo("Pass",CustomMessage="External ID Included in Exported Excel for All reports")
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="External ID Not Included in Exported Excel for report:",Parameter1=result)                           
  
  def VerifyExcelInclExternalIdUnConsolidated():
    Log.Message("VerifyExcelInclExternalIdUnConsolidated")
    
  def VerifyExcelNoDataConsolidated():
    Log.Message("VerifyExcelNoDataConsolidated")
    
  def VerifyExcelNoDataUnConsolidated():
    Log.Message("VerifyExcelNoDataUnConsolidated")
    
  def enterParam(self,ParamList,paramStr):
    paramList = StringParser.splitStr(paramStr,";")
    repInqNum = paramList[0]
    paramList = paramList[1:]
    for param in paramList:
      ReportPackage.ProcRepParamArgs(repInqNum,param)

  def ProcRepParamArgs(repInqNum,arg):
    ObjAction = RepAct()
    items = StringParser.splitStr(arg,"=")
    if len(items) != 1 :
      Log.Message("Entering Parameters for Report: " + arg)
      return
    
    case = StringParser.remAllWhiteSpaces(items[0])
    if case == "acctid":
      acctid = StringParser.remAllWhiteSpaces(items[1])
      tempSelector = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("ListAllAccountBtn"),"REPINQ",str(repInqNum))
      ObjAction.Click(tempSelector)
      
      Log.Message("Wait for List All accounts dialog to open")
      tempSelector = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("ListAllAccountsSearchbar"),"REPINQ",str(repInqNum))
      ObjAction.Sync(tempSelector)
      
      Log.Message("Enter Acct id to search")
      ObjAction.ObjectKeyIn(tempSelector,acctid)
      TestComplete.hardWait(4000,"Wait some time for spinner to go away")
      
      Log.Message("Select first account that comes up after search")
      tempSelector = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("ListAllAccFirstRecSelect"),"REPINQ",str(repInqNum))
      ObjAction.Click(tempSelector)
    
    elif case == startdate:
      startdate = StringParser.remAllWhiteSpaces(items[1])
      Log.Message("Entering From/Start Date for: " + str(repInqNum))
      tempSelector = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("StartDate"),"REPINQ",str(repInqNum))
      ObjAction.ObjectKeyIn(tempSelector,startdate)
      
    elif case == enddate:
      enddate = StringParser.remAllWhiteSpaces(items[1])
      Log.Message("Entering AsOf/End Date for: " + str(repInqNum))
      tempSelector = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("EndDate"),"REPINQ",str(repInqNum))
      ObjAction.ObjectKeyIn(tempSelector,enddate)
      
    elif case == repbasis:
      repbasis = StringParser.remAllWhiteSpaces(items[1])
      Log.Message("Select Report Basis for: " + str(repInqNum)) 
      tempSelector = WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("RepBasis"),"REPINQ",str(repInqNum))
      ObjAction.ListItem(tempSelector,"200")
      
    elif case == currency:
      curr = StringParser.remAllWhiteSpaces(items[1])
      Log.Message("Select Currency for: " + str(repInqNum))
      tempSelector =  WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("Currency"),"REPINQ",str(repInqNum))
      ObjAction.ListItem(tempSelector,curr)
          
    elif case == datetype:
      datetype = StringParser.remAllWhiteSpaces(items[1])
      Log.Message("Select Date Type for: " + str(repInqNum))
      tempSelector =  WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("DateType"),"REPINQ",str(repInqNum))
      ObjAction.ListItem(tempSelector,datetype)
      
    elif case == productline:
      productline = StringParser.remAllWhiteSpaces(items[1])
      Log.Message("Select Product Line for: " + str(repInqNum))
      tempSelector =  WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("ProductLine"),"REPINQ",str(repInqNum))
      ObjAction.ListItem(tempSelector,productline)
      
    elif case == accounttype:
      accounttype = StringParser.remAllWhiteSpaces(items[1])
      Log.Message("Select Product Line for: " + str(repInqNum))
      tempSelector =  WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("AccountType"),"REPINQ",str(repInqNum))
      ObjAction.ListItem(tempSelector,accounttype)
      
    elif case == clientgroup:
      clientgroup = StringParser.remAllWhiteSpaces(items[1])
      Log.Message("Select Client Group for: " + str(repInqNum))
      tempSelector =  WebObjectHandler.UpdateObjProperty(WebObject.getPropertyList("ClientGroup"),"REPINQ",str(repInqNum))
      ObjAction.ListItem(tempSelector,clientgroup)


  def verifyNumOfExpFiles(self,PropList,repNum):
    zipFileName = ReportPackage.DwnExpFileName
    from FileIO import FileIO
    destDir = os.path.join("C:\\Temp\\", os.getlogin() + "_autoTemp")
    FileIO.emptyDir(destDir)
    #Log.Message("destDir=" + destDir)
    #Log.Message("BaseFileName"+FileIO.getFileBaseName(FileIO.getFileNameFromPath(zipFileName)))
    zipDestpath = os.path.join(destDir,FileIO.getFileBaseName(FileIO.getFileNameFromPath(zipFileName)))
    FileIO.createDir(zipDestpath)
    Log.Message("zipFileName: " + zipFileName)
    Log.Message("zipDestpath " + zipDestpath)
    ReportPackage.RepUnzipFile(zipFileName,zipDestpath)
    unZipFileList = FileIO.getFileList(zipDestpath)
    Log.Message("Unzipped file list: " + str(unZipFileList))
    Log.Message("No of files unzipped: " + str(len(unZipFileList)))
    if len(unZipFileList) == int(repNum):
      LoggerHandler.LogInfo("Pass",CustomMessage="Unconsolidated exported Zip contains correct number of file",Parameter1="Expected: " + str(repNum),Parameter2="Actual: " + str(len(unZipFileList)))
    else:
      LoggerHandler.LogInfo("Failed",CustomMessage="Unconsolidated exported Zip contains incorrect number of files",Parameter1="Expected: " + str(repNum),Parameter2="Actual: " + str(len(unZipFileList)))

  def VerifyUnconsolExpFileNames(self,ParamList,paramString):
    zipFileName = ReportPackage.DwnExpFileName
    from FileIO import FileIO
    destDir = os.path.join("C:\\Temp\\", os.getlogin() + "_autoTemp")
    FileIO.emptyDir(destDir)
    #Log.Message("destDir=" + destDir)
    #Log.Message("BaseFileName"+FileIO.getFileBaseName(FileIO.getFileNameFromPath(zipFileName)))
    zipDestpath = os.path.join(destDir,FileIO.getFileBaseName(FileIO.getFileNameFromPath(zipFileName)))
    FileIO.createDir(zipDestpath)
    Log.Message("zipFileName: " + zipFileName)
    Log.Message("zipDestpath " + zipDestpath)
    ReportPackage.RepUnzipFile(zipFileName,zipDestpath)
    unZipFileList = FileIO.getFileList(zipDestpath)
    expFilelist = StringParser.splitStr(paramString,",")
    paramCount = len(expFilelist)
    if len(unZipFileList) != paramCount:
      LoggerHandler.LogInfo("Failed",CustomMessage="Expected File count mismatch",Parameter1="Expected: " + str(paramCount) + " Actual: " + str(repCount))
    OnlyinExp = 0
    for unzipFile in unZipFileList:
      onlyInAct = 0
      for i in range (0, len(expFilelist)-1):
        expFileName = ReportPackage.RepPackageName + "-" + expFilelist[i]
        actFileName = FileIO.getFileBaseName(unzipFile)
        if expFileName == actFileName:
          LoggerHandler.LogInfo("Pass",CustomMessage="Exported File name matches",Parameter1="Expected: " + expFileName + " Actual: " + actFileName)
          break
        else:
          onlyInAct = onlyInAct + 1
      if onlyInAct == paramCount:
        LoggerHandler.LogInfo("Pass",CustomMessage="Exported File Name mismatch",Parameter1="ExpectedList: " + paramString + " Actual: " + actFileName)
        
    
  def RepUnzipFile(FilePath,DestPath):
  	  import zipfile
  	  zip_ref = zipfile.ZipFile(FilePath, 'r')
  	  zip_ref.extractall(DestPath)
  	  zip_ref.close()

#sub testRP
#'  1894:NULL:NULL:12/31/2014:Premis Capital Partners
#  dim ObjRepoObj
#  set DriverLib.PerfLogs = CreateObject("System.Collections.ArrayList")
#  set PageObj = Sys.Browser(TESTBROWSER).Page("https://qa.ims.ea.corp.seic.com*")
#  log.Message PageObj.URL
#  aqutils.Delay 3000
#  set ParObj = PageObj
#  set ObjRepoObj = CreateObject("Scripting.Dictionary") 
#  call CreateObjRepo(ObjRepoObj, "RPObjRep", "D:\Aazim\UIFramework\MDB_UDF\Inputfile\REPORTPACKAGE.xls")
#  set DriverLib.OBJREPO = ObjRepoObj
#  Call DriverLib.UDF_Operations("CLICK",Baselib.getObjSelector("ListAllAcc2766"),NULL,NULL,"NULL",NULL, NULL)
#end sub
#
#