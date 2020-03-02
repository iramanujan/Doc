from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from GenericLibraries.Web import WebActions, WebElementSearch
from Scripts.TestItems import BrowserActions, StaticData
import time

driver = None
def linksTest():
    global driver
    driver = BrowserActions.launchBrowser("firefox",StaticData.strFirefoxpath)
    driver.implicitly_wait(5)
    driver.minimize_window()
    BrowserActions.navigateToPage(driver,"https://www.guru99.com/selenium-tutorial.html")

    objElement = WebElementSearch.find_element(driver,"linktext","What is Selenium WebDriver? Difference with RC")


    print(WebActions.get_linkText(objElement))
    print(WebActions.get_link_href(objElement))
    WebActions.click_link(objElement)
    driver.back()