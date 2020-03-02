from TestComplete import TestComplete
class FindElement:
  	
	def __init__(self):
		Log.Message("Initializing FindElement Class")

	def FindElementByQuerySelector(QuerySelector):
		WebElement = None
		IFrame	= None
		ArrIFrame = None
		try:
		  TestComplete.setObjPage()
		  ObjPage = TestComplete.ObjPage
		  if(ObjPage is not None):
		    #aqUtils.Delay(2000,"Search Object: "+QuerySelector)
		    ArrIFrame = ObjPage.QuerySelectorAll("iframe")
		    if(ArrIFrame is not None):
		      for Index in range (0,len(ArrIFrame)):
		        IFrame = ArrIFrame[Index]
		        if(IFrame is not None):
		          WebElement = IFrame.QuerySelector(QuerySelector)
		          if(WebElement is not None):
		            return WebElement
		          else:
		            iframe2 = IFrame.QuerySelector("#reportViewerIframe")
		            if(iframe2 is not None):
		              WebElement = iframe2.QuerySelector(QuerySelector)
		              if(WebElement is not None):
		                return WebElement
		    WebElement = ObjPage.QuerySelector(QuerySelector)
		finally:
		  return WebElement

	def FindElementsByQuerySelector(QuerySelector):
		WebElement = None
		IFrame	= None
		ArrIFrame = None
		
		try:
		  TestComplete.setObjPage()
		  ObjPage = TestComplete.ObjPage
		  if(ObjPage is not None):
		    #aqUtils.Delay(1000,"Search Object: "+QuerySelector)
		    WebElement = ObjPage.QuerySelectorAll(QuerySelector)
		    if(WebElement is None):
		      ArrIFrame = ObjPage.QuerySelectorAll("iframe")
		      if(ArrIFrame is not None):
		        for Index in range (0,len(ArrIFrame)):
		          IFrame = ArrIFrame[Index]
		          if(IFrame is not None):
		            WebElement = IFrame.QuerySelectorAll(QuerySelector)
		            return WebElement.tolist()
		          else:
		            iframe2 = IFrame.QuerySelector("#reportViewerIframe")
		            if(iframe2 is not None):
		              WebElement = iframe2.QuerySelectorAll(QuerySelector)
		              if(WebElement is not None):
		                return WebElement.tolist()
		finally:
		  if(WebElement is not None):
		    return list(WebElement)
		  else:
		    return WebElement
	  
	def FindElementByXpath(XpathSelector):
		WebElement = None
		IFrame	= None
		ArrIFrame = None
		
		try:
		  TestComplete.setObjPage()
		  ObjPage = TestComplete.ObjPage
		  if(ObjPage is not None):
		    #aqUtils.Delay(1000,"Search Object: "+XpathSelector)
		    WebElement = ObjPage.EvaluateXPath(XpathSelector)
		    if(WebElement is not None):
		      return WebElement[0];
		finally:
		  if(WebElement is not None):
		    return WebElement[0];
		  else:
		    return WebElement

	def FindElementsByXpath(XpathSelector):
		WebElements = None
		IFrame	= None
		ArrIFrame = None
		
		try:
		  TestComplete.setObjPage()
		  ObjPage = TestComplete.ObjPage
		  if(ObjPage is not None):
		    aqUtils.Delay(1000,"Search Object: "+XpathSelector)
		    WebElements = ObjPage.EvaluateXPath(XpathSelector)
		    if(WebElements is not None):
		      return WebElements;
		finally:
		  return WebElements
		      	
	def FindElementByJQuery(QuerySelector):
	  try:
	    JQSelector 	= 	QuerySelector.split(";")[0]
	    Text 		= 	QuerySelector.split(";")[1]
	    WebElement 	= 	None
	    WebElements = 	None

	    if(TestComplete.ObjPage is None):return None;
		
	    ImsContent = TestComplete.ObjPage.QuerySelector("#imsContent")
	    if(ImsContent is not None):
	      WebElements = ImsContent.contentDocument.Script.jQuery(JQSelector)
	      if(WebElements.length > 0):
	        WebElement = FindElement.FindElementByText(WebElements,Text)
	        return WebElement;
			
		
	    WebElements = TestComplete.ObjPage.contentDocument.Script.jQuery(JQSelector)
	    if(WebElements.length > 0):
	      WebElement = FindElement.FindElementByText(WebElements,Text)
	      return WebElement;
	  finally:
	    return WebElement
  
	def FindElementByText(WebElements,Text):
	  WebElement = None
	  try:
	    if(WebElements is not None ):
	      for Index in range (0,WebElements.length):
	        Element = WebElements.get(Index)
	        if(Element is not None):
	          if(Element.textContent == Text):
	            WebElement = Element
	            Log.Message("Element Found: " + Element.outerHTML)
	            return WebElement
	  finally:
	    return WebElement;
	  
	def FindElementSkip(FindPara1,FindPara2):
	  return ""
	
	def FindElementByNameMapping(NameMapSelector):
	  WebElement = None
	  try:
	    if NameMapSelector.Exists:
	      WebElement = NameMapSelector
	  finally:
	    return WebElement