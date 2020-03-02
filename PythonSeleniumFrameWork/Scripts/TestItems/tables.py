from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from GenericLibraries.Web import WebActions, WebElementSearch, WebTables
from Scripts.TestItems import BrowserActions, StaticData
import time
driver = None
def tablestest():
    global driver
    driver = BrowserActions.launchBrowser("firefox",StaticData.strFirefoxpath)
    driver.implicitly_wait(5)
    driver.minimize_window()
    BrowserActions.navigateToPage(driver,"https://testautomationpractice.blogspot.com/")

    objElement = WebElementSearch.find_element(driver,"name","BookTable")

    print(WebTables.get_table_rowCount(objElement))
    print(WebTables.get_table_colCount(objElement,3))
    print(WebTables.get_table_cellData_byIndex(objElement,3,2))
    WebTables.click_table_cell_byValue(objElement,"Amod")
    listD = WebTables.get_webTable_data(objElement)
    print(listD)
    print("----------------------------------------")
    for item in listD:
        print(str(item))