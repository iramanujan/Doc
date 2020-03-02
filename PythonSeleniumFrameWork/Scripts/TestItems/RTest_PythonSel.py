from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import datetime

# project related libraries import
from GenericLibraries.Web import WebElementSearch
from GenericLibraries.Web import WebActions



def test_seltest1():
    try :
        strChromePath = "D:\Learning POCs\Python\PythonSeleniumFrameWork\webdrivers\chromedriver.exe"
        strIEPath = "D:\Learning POCs\Python\PythonSeleniumFrameWork\webdrivers\IEDriverServer.exe"
        strFirefoxpath = "D:\Learning POCs\Python\PythonSeleniumFrameWork\webdrivers\geckodriver.exe"
        #strEdgepath = "D:\Learning POCs\Python\PythonSeleniumFrameWork\webdrivers\msedgedriver.exe"
        print(strChromePath)
        # #driver = webdriver.Chrome(strChromePath)
        driver = webdriver.Firefox( executable_path = strFirefoxpath)
        driver.implicitly_wait(3) # implicit wait
        # #driver = webdriver.Ie(strIEPath)
        # #driver = webdriver.Edge(strEdgepath)
        driver.get("https://www.google.com/")
        #
        webElement = driver.find_element_by_name("q")
        webElement.send_keys("Selenium with Python")
        webElement.send_keys(Keys.ENTER)
        print(datetime.datetime.now())
        #time.sleep(3)
        ## explicit wait for element
        #wait = WebDriverWait(driver,20)
        #element = wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="resultStats"]')))
        strSearchResult = driver.find_element(By.ID,"resultStats")#driver.find_element_by_xpath('//*[@id="resultStats"]')
        # #expected_conditions.element_to_be_clickable
        print(datetime.datetime.now())
        print(strSearchResult.text)
        #print(element.text)

        WebActions.check_checkBox(driver)
        #driver.find_element_by_partial_link_text("Selenium").click()
        #driver.back() # for back page
        #time.sleep(5)
        #driver.forward() # for forward action
    except Exception :
        print("Exception " + str(datetime.datetime.now()))
        print(str(Exception))