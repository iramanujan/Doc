from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from GenericLibraries.Web import WebActions, WebElementSearch
from Scripts.TestItems import BrowserActions, StaticData
import time

def dropdownt():


    driver = BrowserActions.launchBrowser("firefox", StaticData.strFirefoxpath)
    driver.implicitly_wait(5)
    driver.minimize_window()
    BrowserActions.navigateToPage(driver,"https://testautomationpractice.blogspot.com/")

    objElement = WebElementSearch.find_element(driver,"name","products")


    WebActions.selectItem_dropDown(objElement, "Bing", "byvisibletext")
    print(WebActions.getSelectedItemValue_dropDown(objElement))
    print(WebActions.getItems_dropDown(objElement))
    print(WebActions.getItem_Count_dropDown(objElement))
    #WebActions.clearSelection_dropDown(objElement)
    print(WebActions.getItemIndex_dropDown(objElement, "Google"))


