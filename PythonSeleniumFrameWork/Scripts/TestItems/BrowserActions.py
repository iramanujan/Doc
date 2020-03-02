from selenium import webdriver
def launchBrowser(strBrowserName, strBrowserpath):
    if(strBrowserName.lower() == "chrome"):
        return webdriver.Chrome(executable_path = strBrowserpath)
    if(strBrowserName.lower() == "ie"):
        return webdriver.Ie(executable_path = strBrowserpath)
    if(strBrowserName.lower() == "firefox"):
        return webdriver.Firefox(executable_path = strBrowserpath)
    if(strBrowserName.lower() == "edge"):
        return webdriver.Edge(executable_path = strBrowserpath)

def navigateToPage(driver,strUrl):
    driver.get(strUrl)

def closeBrowser(driver):
    driver.close()