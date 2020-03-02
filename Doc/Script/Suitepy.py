import os
class Suite:
  ObjectRepositoryMapping = {};
  ApplicationMapping = {};  


  def __init__(self):
    Log.Message("Initializing Suite Class");
    self.ObjectRepositoryMapping = {
        "MDBPROMONITOR":"MDBObjRep",
        "MDBFULLREG":"MDBObjRep",
        "MDBFULLREGQA":"MDBObjRep",
        "NEWMDBFULLREGQA":"MDBObjRep",
        "MDBFULLREGPILOT":"MDBObjRep",
        "MDBPRODSMOKE":"MDBObjRep",
        "MDBQADATACOMP":"MDBObjRep",
        "MDBPILOTDATACOMP":"MDBObjRep",
        "RDLREP":"MDBObjRep",
        "MDBSCHED":"SCHEDObjRep",
        "INSIGHTREP":"MDBObjRep",
        "INSIGHTREPSMOKE":"MDBObjRep",
        "INSIGHTREPDATCOMP":"MDBObjRep",
        "INSIGHTSCHED":"SCHEDObjRep",
        "INSIGHTPROC":"INSIGHTObjRep",
        "INSIGHTUIREG":"INSIGHTObjRep",
        "INSIGHTUISMOKE":"INSIGHTObjRep",
        "INSIGHTTRANUIREG":"INSIGHTObjRep",
        "UDFQA":"UDFObjRep",
        "UDFPILOT":"UDFObjRep",
        "UDFPROD":"UDFObjRep",
        "UDFSMOKE":"UDFObjRep",
        "ECRINTREG":"ECRObjRep",
        "ECREXTREG":"ECRObjRep",
        "FORMPF":"FORMPFObjRep",
        "SMOKEFORMPF":"FORMPFObjRep",
        "FORMPFSETUP":"FORMPFObjRep",
        "AIFMD":"AIFMDObjRep",
        "AIFMDSMOKE":"AIFMDObjRep",  
        "CPOPQRREG":"CPOPQRObjRep",
        "13F":"13FObjRep",
        "13FSMOKE":"13FObjRep",
        "FATCA":"FATCAObjRep",
        "FATCASMOKE":"FATCAObjRep",
        "PLATADMREG":"PLATADMObjRep",
        "PLATADMSMK":"PLATADMObjRep",
        "PLATADM":"PLATADMObjRep",
        "INVESTRAN":"INVESTRANObjRep",
        "ECRINPUT":"ECRObjRep",
        "ECROUTPUT":"ECRObjRep",
        "REPORTPACKAGEREG":"RPObjRep",
        "REPORTPACKAGEREGSCH":"RPObjRep",
        "DDTREPPACKAGE":"RepObjRep",
        "DDTECR":"ObjRep",
        "DDTECRPRIVATEFUND":"PFObjRep",
        "WORKDESKQA":"WORKDESKObjRep",
    }
    self.ApplicationMapping ={
        "MDBObjRep":"MDB",
        "UDFObjRep":"UDF",
        "ECRObjRep":"ECR",
        "FORMPFObjRep":"FORMPF",
        "AIFMDObjRep":"AIFMD",
        "CPOPQRObjRep":"CPOPQR",
        "PLATADMObjRep":"PLATADM",
        "INSIGHTObjRep":"INSIGHT",
        "SCHEDObjRep":"SCHEDULECR",
        "INVESTRANObjRep":"Investran",
        "FATCAObjRep":"FATCA",
        "RPObjRep":"REPORTPACKAGE",
        "RepObjRep":"DDTREPPACKAGE",
        "ObjRep":"DDTECR",
        "PFObjRep":"DDTECRPRIVATEFUND",
        "WORKDESKObjRep":"WORKDESK",
    }
    
  def GetObjectRepositoryName(self,SuiteToRun):
    ObjectRepositoryName = self.ObjectRepositoryMapping.get(aqString.ToUpper(SuiteToRun), "")
    return ObjectRepositoryName
    
  def GetFileName(self,SuiteToRun):
    ObjectRepositoryName = self.GetObjectRepositoryName(SuiteToRun)
    FileName = self.ApplicationMapping.get(ObjectRepositoryName, "")
    return FileName
    
  def GetFilePath(self,SuiteToRun):
    #RootDir = Project.Path+"TestRepo\\TestSuite"
    from TestConfig import TestConfig
    RootDir = Project.Path+"..\\..\\TestInput"
    TestConfig.InputFilePath = RootDir
    FileName = self.GetFileName(SuiteToRun);
    for root, dirnames, filenames in os.walk(RootDir):
      for File in filenames:
        if(aqString.ToLower(os.path.splitext(File)[0]) == aqString.ToLower(FileName)):
          return os.path.join(root, File)