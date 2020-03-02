from FindElement import FindElement

class By:
  SelectorType = {}
  def __init__(self):
    self.SelectorType = {
										"XPATH" 											:	FindElement.FindElementByXpath,
										"XPATHALL" 										:	FindElement.FindElementsByXpath,
										"QUERYSELECTOR" 							:	FindElement.FindElementByQuerySelector,
										"QUERYSELECTORALL" 						:	FindElement.FindElementsByQuerySelector,
										"JQUERYTEXTFIND" 							:	FindElement.FindElementByJQuery,
										"QUERYSELECTORTXT" 						:	"",
										"GETOBJBYTEXT" 								:	"",
										"GETOBJBYTAGNAMEANDTEXT" 			:	"",
										"NAMEMAPPING"                 : FindElement.FindElementByNameMapping,
										"SKIPFIND" 									  :	FindElement.FindElementSkip
								}