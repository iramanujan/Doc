from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from GenericLibraries.Web import WebActions, WebElementSearch
from Scripts.TestItems import BrowserActions, StaticData
import time

def checkboxTest():

    driver = BrowserActions.launchBrowser("firefox",StaticData.strFirefoxpath)
    driver.implicitly_wait(5)
    driver.minimize_window()
    BrowserActions.navigateToPage(driver,"https://testautomationpractice.blogspot.com/")

    time.sleep(10)

    #radioButtonGrp = WebElementSearch.find_element(driver,"xpath","//*[@value='Radio-0']")
    #radioButtonGrp.click()

    driver.find_element_by_id("RESULT_CheckBox-8_0").click()
    #objCheckbox = WebElementSearch.find_element(driver,"id",'RESULT_CheckBox-8_1')
    #objCheckbox.click()

def radio():
    pass