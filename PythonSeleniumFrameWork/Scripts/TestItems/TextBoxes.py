from selenium import webdriver
from selenium.webdriver import ActionChains

from GenericLibraries.Web import WebActions, WebElementSearch
from Scripts.TestItems import BrowserActions, StaticData
import time
driver = None
def verify_textBoxes():
    global driver
    driver = BrowserActions.launchBrowser("firefox",StaticData.strFirefoxpath)
    driver.minimize_window()
    BrowserActions.navigateToPage(driver,"https://testautomationpractice.blogspot.com/")

    objButton = WebElementSearch.find_element(driver,"xpath","//*[contains(text(),'Copy Text')]")

    WebActions.double_click_button(driver,objButton)

    objField1 = WebElementSearch.find_element(driver,"id","field1")
    objField2 = WebElementSearch.find_element(driver,"id","field2")


    print(driver.find_element_by_id("field1").get_attribute('value'))


    strF2 = WebActions.getValue_textBox(objField2)
    strF1 = WebActions.getValue_textBox(objField1)
    print("Data after copy is not same Expected :" + strF1 + " Actual :"+ strF2)
    assert (strF2 == strF1),"Data after copy is  Expected :" + strF1 + " Actual :"+ strF2
    time.sleep(2)
    WebActions.clear_textBox(objField2)
    time.sleep(2)
    WebActions.setValue_textBox(objField2,"PKTesting")
    objField2 = WebElementSearch.find_element(driver,"id","field2")
    strF2 = WebActions.getValue_textBox(objField2)
    print("Data after update is not same, Expected :" + "PKTesting" + " Actual :"+ strF2)
    assert (strF2 == "PKTesting"),"Data after update , Expected :" + "PKTesting" + " Actual :"+ strF2