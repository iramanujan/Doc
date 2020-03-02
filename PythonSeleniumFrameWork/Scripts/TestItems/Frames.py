from selenium import webdriver
from selenium.webdriver.common.by import By

from GenericLibraries.Web import WebActions, WebElementSearch
from Scripts.TestItems import StaticData, BrowserActions

def framesTest():

    driver = BrowserActions.launchBrowser("firefox",StaticData.strFirefoxpath)
    driver.implicitly_wait(5)
    driver.minimize_window()
    BrowserActions.navigateToPage(driver,'https://selenium.dev/selenium/docs/api/java/index.html')


    WebActions.switch_toFrame(driver,"packageListFrame")
    WebElementSearch.find_element(driver,"linktext","org.openqa.selenium.firefox.internal").click()
    WebActions.switch_toMainFrame(driver)

    WebActions.switch_toFrame(driver,"packageFrame")
    WebElementSearch.find_element(driver,"linktext","Executable").click()

    WebActions.switch_toMainFrame(driver)
    # WebActions.switch_toFrame(driver,"classFrame")
    # WebElementSearch.find_element(driver,"xpath","//*[contains(text(),'TREE')]").click()
