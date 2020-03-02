import sys

import camelot


def convert_pdf_into_json(strPdfExportLocation,strJsonFileLocation):
    data = camelot.read_pdf(strPdfExportLocation,pages='all', flavor='stream', flag_size=True)
    data.export(strJsonFileLocation, f='json')
  #camelot.read_pdf(strPdfExportLocation,pages='all',flavor='lattice',flag_size=True).export(strJsonFileLocation,f='json')



strPdfExportLocation = r'D:\\Office\\Code\\Master-PDF\\CitiXsysAutomation\\Citixsys_Regression\\ExportedReport\\SalesByTransactionType\\SalesByTransactionType.pdf'
strJsonFileLocation = r'D:\\Office\\Code\\Master-PDF\\CitiXsysAutomation\\Citixsys_Regression\\ExportedReport\\SalesByTransactionType\\SalesByTransactionType.json'

#convert_pdf_into_json(strPdfExportLocation,strJsonFileLocation)



def combine_two_dictionary_value_into_list(dict1,dict2):
    for key in dict1:
        if key in dict2:
            dict1[key] = dict1[key] + dict2[key]
    return dict1


def convert_dictionary_value_into_list(dict):
    for key, value in dict.items():
        dict[key] = [value for key2, value in dict.items() if (key == key2)]
    return dict


dict1 = {"A":1,"B":2}
#dict1 = convert_dictionary_value_into_list(dict1)

dict2 = {"A":3,"B":4}
#dict2 = convert_dictionary_value_into_list(dict2)

dict3 = {"A":3,"B":4}
dict4 = {"A":3,"B":4}
#dict3 = convert_dictionary_value_into_list(dict3)

def convet_dictionary_into_dataframe(dict1,dict2,dict3,dict4,strFileName, strSheetName,strFilePath = "D:/"):
  import sys
  import pandas as pd
  d1 = pd.DataFrame([dict1])
  d2 = pd.DataFrame([dict2])
  d3 = pd.DataFrame([dict3])
  d4 = pd.DataFrame([dict4])
  df = pd.concat([d1, d2, d3, d4], ignore_index=True)
  writer = pd.ExcelWriter(strFilePath+strFileName+'.xlsx', engine='xlsxwriter')
  df.to_excel(writer, sheet_name=strSheetName)
  writer.save()

#convet_dictionary_into_dataframe(dict1,dict2,dict3,dict4,"ss",'ss')

import json
import os
def read_json_file(strJsonFilePath):
    fileName, fileExtension = os.path.splitext(strJsonFilePath)
    strfile = "page-1-table-1"
    with open(fileName + strfile + fileExtension) as json_file:
        data = json.load(json_file)
    print(data)



import pandas as pd
excelFilePath = r'D:\Sales.xlsx'
df = pd.read_excel(excelFilePath,sheet_name='Sales',dtype = 'object')

print(df)