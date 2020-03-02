import copy
import math
# Data from excel will be pased on this object to standardize input. This will allow to change the structure of excel freeely without affecting test cases
class TCParser:
  tcHeader = None
  testCaseSheetRec = None
  testCaseDataRec = None
  
  normalizeTCRecSet = {}
  
  def __init__(self,tcRecords,tcDataRecs=None):
    self.testCaseSheetRec = tcRecords
    self.testCaseDataRec = tcDataRecs
    self.tcHeader = self.getListHeaderDict(self.testCaseSheetRec)
    
  def getListHeaderDict(self,inputList):
    Header = {}
    HeadRec = inputList[0]
    for colHead in HeadRec:
      if colHead is not None:
        Header[VarToString(colHead)]=HeadRec.index(colHead)
    return Header
  
  #This is to Parse Regular TC input records
  def regInputTCParser(self):
    #Read header and decide what are column names and their positions
    shHeader = self.tcHeader
    headerRow = self.testCaseSheetRec[0]
    tcId = headerRow[shHeader['TC ID']]
    for row in self.testCaseSheetRec:
      if row[shHeader['TC ID']] not in ("TC ID","NONE",""):
        tcId = row[shHeader['TC ID']]
      if row[shHeader['ExecCond']] not in ("n","N","","ExecCond"):
        listWotcid = row[0:shHeader['TC ID']] + row[shHeader['TC ID']+1:]
        finalList = listWotcid[0:shHeader['ExecCond']] + listWotcid[shHeader['ExecCond']+1:]
        if tcId not in self.normalizeTCRecSet:
          self.normalizeTCRecSet[tcId] = []
        self.normalizeTCRecSet[tcId].append(finalList)
        #Code can be added later on to create a Queue of LOGREPORT messages
    #reset header according to new list
    hdRowWoTcId = headerRow[0:shHeader['TC ID']] + headerRow[shHeader['TC ID']+1:]
    hdRowWoExCnd = hdRowWoTcId[0:shHeader['ExecCond']] + hdRowWoTcId[shHeader['ExecCond']+1:]
    finalHdRow = []
    finalHdRow.append(hdRowWoExCnd)
    self.tcHeader = self.getListHeaderDict(finalHdRow)   
    return self.normalizeTCRecSet

  #Creates list of test steps required for the testcase
  def flatDDTTestCase(self,TestCaseRecs,TdRow,TdHeader):
    shHeader = self.getListHeaderDict(TestCaseRecs)
    finalTCList = []
    for row in TestCaseRecs:
      #if row[shHeader['TC_STEP']] != 'TC_STEP':
      if row[shHeader['Override']] !=0:
        argval = row[shHeader['Override']]
      else:
        tdkey = row[shHeader['Param1']]
        if tdkey in TdHeader:
            argval = TdRow[TdHeader[tdkey]]
        else:
            argval = "N"
        row[shHeader['Param1']] = argval
      if row[shHeader['ACTION']] in ("TCBEGIN","TCEND"):
          row[shHeader['TC_STEP']] = TdRow[TdHeader["Test Case Desc"]]
      if row[shHeader['Param1']] not in ("n","N","","Override"):
          finalTCList.append(row[0:shHeader['Override']] + row[shHeader['Override']+1:])
    self.tcHeader = self.getListHeaderDict(finalTCList)
    return finalTCList[1:]
    
 
  def ddtInputTCParser(self):
    #Read rows of Environment parameter and Execute Condition
    Log.Message("testcaserec",str(self.testCaseDataRec))
    envparam = self.testCaseDataRec[2]
    execCond = self.testCaseDataRec[3]
    #Find out how many tests to execute
    tcToexec = []
    for i,env in enumerate(envparam):
        if env == "QA":
            execCondCol = execCond[i]
            if execCondCol == "yes":
                tcToexec.append(i)
    #Transpose row and columns
    transposeTestData = []
    transposeTestData.append(list(zip(*self.testCaseDataRec))[0])#2
    for ele in tcToexec:
        transposeTestData.append(list(zip(*self.testCaseDataRec))[ele])
    ddtTCRow = []
    shHeader = self.getListHeaderDict(transposeTestData)

    tcId = transposeTestData[0][shHeader['TC ID']]
    for row in transposeTestData:
      if row[shHeader['TC ID']] != 'TC ID':
        rowDict={}
        if row[shHeader['TC ID']] != "NONE":
          tcId = row[shHeader['TC ID']]
        currTcList = copy.deepcopy(self.testCaseSheetRec)
        ddtTCRow = self.flatDDTTestCase(currTcList,row,shHeader)
        if tcId not in self.normalizeTCRecSet:
          self.normalizeTCRecSet[tcId] = ddtTCRow

    return self.normalizeTCRecSet
    
  def ddtInputTCParser_old(self):
    #Read rows of Environment parameter and Execute Condition
    envparam = self.testCaseDataRec[2]
    execCond = self.testCaseDataRec[3]
    #Find out how many tests to execute
    tcToexec = []
    for i,env in enumerate(envparam):
        if env == "QA":
            execCondCol = execCond[i]
            if execCondCol == "yes":
                tcToexec.append(i)
    #Transpose row and columns
    transposeTestData = []
    transposeTestData.append(list(zip(*self.testCaseDataRec))[2])
    for ele in tcToexec:
        transposeTestData.append(list(zip(*self.testCaseDataRec))[ele])

    ddtTCRow = []
    shHeader = self.getListHeaderDict(transposeTestData)

    tcId = transposeTestData[0][shHeader['TC ID']]
    for row in transposeTestData:
      if row[shHeader['TC ID']] != 'TC ID':
        rowDict={}
        if row[shHeader['TC ID']] != "NONE":
          tcId = row[shHeader['TC ID']]
        for key,value in shHeader.items():
          if(key != "TC ID"):
            rowDict[key] = row[value]
        ddtTCRow = self.flatDDTTestCase(self.testCaseSheetRec,rowDict)
        if tcId not in self.normalizeTCRecSet:
          self.normalizeTCRecSet[tcId] = ddtTCRow

    return self.normalizeTCRecSet
    
#========================================== OLD CODE TO REMOVE AFTER TESTING ========================================================
  def regInputTCParser_old(self):
    #Read header and decide what are column names and their positions
    shHeader = self.getListHeaderDict(self.testCaseSheetRec)
    
    tcId = self.testCaseSheetRec[0][shHeader['TC ID']]
    for row in self.testCaseSheetRec:
      if row[shHeader['TC ID']] != 'TC ID':
        rowDict={}
        if row[shHeader['TC ID']] != "NONE":
          tcId = row[shHeader['TC ID']]
        for key,value in shHeader.items():
          if(key != "TC ID"):
            rowDict[key] = row[value]
        if tcId not in self.normalizeTCRecSet:
          self.normalizeTCRecSet[tcId] = []
        self.normalizeTCRecSet[tcId].append(rowDict)
        #Code can be added later on to create a Queue of LOGREPORT messages    
    return self.normalizeTCRecSet
    
def regInputTCParser(self):
    #Read header and decide what are column names and their positions
    shHeader = self.tcHeader
    
    tcId = self.testCaseSheetRec[0][shHeader['TC ID']]
    for row in self.testCaseSheetRec:
      if row[shHeader['TC ID']] != "NONE":
        tcId = row[shHeader['TC ID']]
      if tcId not in self.normalizeTCRecSet:
        self.normalizeTCRecSet[tcId] = []
      if row[shHeader['ExecCond']] not in ("n","N","","ExecCond"):
        listWotcid = row[0:shHeader['TC ID']] + row[shHeader['TC ID']+1:]
        finalList = listWotcid[0:shHeader['ExecCond']] + listWotcid[shHeader['ExecCond']+1:]
        self.normalizeTCRecSet[tcId].append(finalList[1:])
        #Code can be added later on to create a Queue of LOGREPORT messages 
    self.tcHeader = self.getListHeaderDict(self.normalizeTCRecSet[tcId])   
    return self.normalizeTCRecSet

def flatDDTTestCase_old(self,TestCaseRecs,TestData):
    shHeader = self.getListHeaderDict(TestCaseRecs)
    finalTCList = []
    for row in TestCaseRecs:
      if row[shHeader['TC_STEP']] != 'TC_STEP':
        rowDict={}
        for key,value in shHeader.items():
            if(key != "Override"):
                if(key == "Param1"):
                    overRide = row[shHeader["Override"]]
                    if(overRide != 0):
                        argval = overRide
                    else:
                        tdkey = row[value]
                        if tdkey in TestData:
                            argval = TestData[tdkey]
                        else:
                            argval = "N"
                else:
                    argval = row[value]
                rowDict[key] = argval
        if rowDict["ACTION"] in ("TCBEGIN","TCEND"):
            rowDict["TC_STEP"] = TestData["Test Case Desc"]
        if rowDict["Param1"] not in ("n","N","","Override"):
            finalTCList.append(rowDict)
    return finalTCList
    