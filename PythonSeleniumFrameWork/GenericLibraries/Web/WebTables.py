from selenium.webdriver.common.by import By


def get_table_rowCount(objTable):
    return len(objTable.find_elements(By.TAG_NAME, "tr"))


def get_table_colCount(objTable, intRowIndex = 0):
    listobjs = objTable.find_elements(By.TAG_NAME, "tr")
    if(intRowIndex > 0):
        return len(listobjs[intRowIndex].find_elements(By.TAG_NAME, "td"))
    return len(listobjs[intRowIndex].find_elements(By.TAG_NAME, "th"))



def get_webTable_data(objTable):
    listRet = []
    listRows = objTable.find_elements(By.TAG_NAME, "tr")
    for row in listRows :
        listCols = row.find_elements(By.TAG_NAME, "td")
        if(len(listCols) == 0):
            continue
        strRowData = ""
        for colIndex in range(len(listCols)) :
            strRowData = strRowData + "," + listCols[colIndex].text if colIndex != 0 else strRowData + listCols[colIndex].text

        listRet.append(strRowData)
    return listRet

def get_webTable_data_2(objTable): # returns in dictionary form
    listdictRet, listColName = [],[]
    listRows = objTable.find_elements(By.TAG_NAME, "tr")
    listObjColNames = listRows[0].find_elements(By.TAG_NAME, "th")
    listColName = list(map(lambda item : item.text, listObjColNames))
    print(listColName)
    for row in listRows :
        listCols = row.find_elements(By.TAG_NAME, "td")
        if(len(listCols)==0):
            continue
        dictR = {}
        for colIndex in range(len(listCols)) :
            dictR[listColName[colIndex]] = listCols[colIndex].text
        listdictRet.append(dictR)
    return listdictRet

def get_table_columnNames():
    pass

def get_table_rowData():
    pass

def get_table_rowIndex():
    pass

def get_table_columnIndex():
    pass

def get_table_cellData_byValue():
    pass

def get_table_cellData_byIndex(objTable, intRowIndex = 0, intColIndex = 0):
    listRows = objTable.find_elements(By.TAG_NAME, "tr")
    strColHead = "th" if intRowIndex==0 else "td"
    listCols = listRows[intRowIndex].find_elements(By.TAG_NAME, strColHead)
    return listCols[intColIndex].text

def click_table_cell_byValue(objTable, strValue):
    listRows = objTable.find_elements(By.TAG_NAME, "tr")
    for row in listRows :
        listCols = row.find_elements(By.TAG_NAME, "td")
        for col in listCols :
            if(col.text == strValue):
                col.click()

def get_table_cell_object(objTable, strCellValue):
    listRows = objTable.find_elements(By.TAG_NAME, "tr")
    for row in listRows:
        listCols = row.find_elements(By.TAG_NAME, "td")
        for col in listCols:
            if (col.text == strCellValue):
                return col
def click_table_cell_byIndex(objTable, intRowIndex, intColIndex):
    listRows = objTable.find_elements(By.TAG_NAME, "tr")
    strColHead = "th" if intRowIndex==0 else "td"
    listCols = listRows[intRowIndex].find_elements(By.TAG_NAME, strColHead)
    listCols[intColIndex].click()