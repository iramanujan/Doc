import re

class StringParser:
  
  def __init__(self, regex):
    self.pattern = regex
  
  def getFirstMatch(pattern,SearchString):
    #compile the regex first
    #pat = re.compile(self.regexp)
    mreslist = re.findall(pattern,SearchString,re.I)
    return mreslist[0]
  
  def getListofAllMatches(pattern,SearchString):
    #compile the regex first
    #pat = re.compile(self.regexp)
    return re.findall(pattern,SearchString,re.I)

  def remAllWhiteSpaces(inpString):
    return "".join(inpString.split())
  
  def remAllSpecialCharacters(inpString):
    return ''.join(e for e in inpString if e.isalnum() or e=="_")
  
  def regexReplace(pattern,inpString,replBy):
    return re.sub(pattern,replBy,inpString,re.I)
  
  def replace(inpString,searchString,replBy):
    return inpString.replace(searchString,replBy)
  
  def TextContains(pattern,searchString):
    return re.search(pattern,searchString,re.I)
  
  def isEmpty(inpString):
    return not inpString.isspace()
    
  def RemoveSpaces(Text):
    if(Text is not None and Text != ""):
      return aqString.Replace(aqString.Trim(Text,aqString.stAll)," ","") 
    else: return "";
    
  def splitStr(inpString, splitDelem=""):
    return inpString.split(splitDelem)
  
  def toLower(inpString):
    return inpString.lower()
    
  def IsEmptyOrNone(InputString):
    if(InputString == None): return False
    elif(not(InputString and InputString.strip())):return False
    else: True