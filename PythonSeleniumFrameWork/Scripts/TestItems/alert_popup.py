from selenium import webdriver
from selenium.webdriver import ActionChains

from GenericLibraries.Web import WebActions, WebElementSearch
from Scripts.TestItems import BrowserActions, StaticData

def alerts():
    driver = BrowserActions.launchBrowser("firefox",StaticData.strFirefoxpath)
    driver.implicitly_wait(10)
    BrowserActions.navigateToPage(driver,"https://testautomationpractice.blogspot.com/")
    objButton = WebElementSearch.find_element(driver,"xpath","//*[contains(text(),'Click Me')]")

    # accept alert
    WebActions.click_button(objButton)
    print("while accepting "+ WebActions.get_alertMessage(driver))
    WebActions.accept_alert(driver)


    # dismiss alert
    WebActions.click_button(objButton)
    print("while dismissing " + WebActions.get_alertMessage(driver))
    WebActions.dismss_alert(driver)