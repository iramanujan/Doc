from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

webdriver = None


# common for objects like getting values for required properties or properties of object
def getPropertyValue_object(object, strPropName):
    return object.get_attribute(strPropName)


def check_objectPresent():
    pass


def check_objectVisible():
    pass


def hover_overObject():
    pass


# for drop down select objects , below are actions
def selectItem_dropDown(objElement, strValue, strValType="byvisibletext"):
    objElement = Select(objElement)
    if (strValType.lower() == "byvisibletext"):
        objElement.select_by_visible_text(strValue)
    elif (strValType.lower() == "byvisibletext"):
        objElement.select_by_index(strValue)
    elif (strValType.lower() == "byvisibletext"):
        objElement.select_by_value(strValue)


def getItems_dropDown(objElement):
    objElement = Select(objElement)
    listElemetns = objElement.options
    listOP = list(map(lambda item: item.text, listElemetns))
    return listOP


def getItem_Count_dropDown(objElement):
    objElement = Select(objElement)
    return len(objElement.options)


def clearSelection_dropDown(objElement):
    objElement = Select(objElement)
    objElement.deselect_all()
    return len(objElement.options)


def getItemIndex_dropDown(objElement, strVisibleText):
    objElement = Select(objElement)
    listElemetns = objElement.options
    for index in range(0, len(listElemetns)):
        if (listElemetns[index].text == strVisibleText):
            return index
    return -1


def getSelectedItemValue_dropDown(objElement):
    return Select(objElement).first_selected_option


# radio buttons ------- to be done
def check_radioButton(bojRadioButton):
    bojRadioButton.click()


def getCurrentCheckStatus_radioButton():
    pass


# checkboxes -----to be done
def check_checkBox(driver):
    webdriver = driver
    webdriver.get("https://www.google.com/")

    pass


def uncheck_checkBox():
    pass


def getCurrentCheckStatus_checkBox():
    pass


# text boxes
def setValue_textBox(objTextBox, strValue):
    objTextBox.send_keys(strValue)


def getValue_textBox(objTextBox):
    return getPropertyValue_object(objTextBox, "value")


def clear_textBox(objTextBox):
    objTextBox.clear()


# buttons
def click_button(objButton):
    objButton.click()


def get_buttonText(objButton):
    return objButton.text


def double_click_button(driver, objButton):
    action = ActionChains(driver)
    action.double_click(objButton).perform()


# link
def click_link(objLink):
    objLink.click()


def get_linkText(objLink):
    return objLink.text


def get_link_href(objLink):
    return getPropertyValue_object(objLink, 'href')


# alerts
def accept_alert(driver):
    driver.switch_to_alert().accept()


def dismss_alert(driver):
    driver.switch_to_alert().dismiss()


def get_alertMessage(driver):
    return driver.switch_to_alert().text


# frames
def switch_toFrame(driver, strFrameName_id):
    driver.switch_to_frame(strFrameName_id)


def switch_toMainFrame(driver):
    driver.switch_to_default_content()


# multiple windows
def switch_toWindow():
    pass


def switch_toMainWindow():
    pass


def get_AllWindowHandles():
    pass
