class ObjRepoParser:
  objRepoSheetRec = None
  objRepo = {}
  
  def __init__(self,objRec):
    self.objRepoSheetRec = objRec
  
  def getDict(objRec):
   for row in objRec:
     ObjRepoParser.objRepo[row[0]] = row[1:]
   return ObjRepoParser.objRepo
   
   #in order to get list of dictionary use unpacking operator *
#   listKeys = [*self.objRepo]
#   for x in listKeys:
#     Log.Message(x)