import os
class ConfigReader:
  configFilePath=Project.Path+"TestRepo\Configs\configuration.properties.txt"
  useDwnFolder = os.path.join(os.environ['USERPROFILE'],"Downloads")
  
  #def __init__(self):
  #      Log.Message(self.configFilePath)
  
  def load_properties(self,configFilePath, sep='=', comment_char='#'):
    try:
      props = {}
      with open(configFilePath, "rt") as f:
          for line in f:
              l = line.strip()
              if l and not l.startswith(comment_char):
                  key_value = l.split(sep)
                  key = key_value[0].strip()
                  value = sep.join(key_value[1:]).strip().strip('"') 
                  props[key] = value 
      return props
    except Exception as e:
      Log.Error(str(e))
      raise
      