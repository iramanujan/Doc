from selenium import webdriver
from selenium.webdriver import ActionChains

from GenericLibraries.Web import WebActions, WebElementSearch
from Scripts.TestItems import BrowserActions, StaticData

def buttons():

    driver = BrowserActions.launchBrowser("firefox",StaticData.strFirefoxpath)
    driver.minimize_window()
    BrowserActions.navigateToPage(driver,"https://testautomationpractice.blogspot.com/")

    objButton = WebElementSearch.find_element(driver,"xpath","//*[contains(text(),'Copy Text')]")

    WebActions.double_click_button(driver,objButton)

