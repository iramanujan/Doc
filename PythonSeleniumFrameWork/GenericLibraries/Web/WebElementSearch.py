from selenium.webdriver.common.by import By

from GenericLibraries.Logging import Generic_Logger


def find_element(driver,strByType, strValue):
    objBy = None
    if(strByType.lower() == "linktext") : objBy = By.LINK_TEXT
    elif (strByType.lower() == "id"): objBy = By.ID
    elif (strByType.lower() == "classname"): objBy = By.CLASS_NAME
    elif (strByType.lower() == "css"): objBy = By.CSS_SELECTOR
    elif (strByType.lower() == "name"): objBy = By.NAME
    elif (strByType.lower() == "partiallinktext"): objBy = By.PARTIAL_LINK_TEXT
    elif (strByType.lower() == "tagname"): objBy = By.TAG_NAME
    elif (strByType.lower() == "xpath"): objBy = By.XPATH
    else :
        Generic_Logger.print_console("no valid input is given")
        return None
    # get object and return
    Generic_Logger.print_console("***************Searching for Element****************** for type: " + str(objBy) + "| with Value:" + strValue)
    try :
        return driver.find_element(objBy,strValue)
    except Exception as e:
        Generic_Logger.print_console("***************No element has been found****************** for type: "+ str(objBy) + "| with Value:"+strValue)
        Generic_Logger.print_console(e)
        return None



def find_elements():
    pass



