import csv
from collections import defaultdict
from xml.dom import minidom
import shutil
import os
from datetime import datetime
import sys

def copy_file(source=r"C:\temp\RegressionResult.csv", destination=r'C:\temp\FailedTestItemsLogs/'):
    try:
        if os.path.exists(source):
            shutil.copy(source, destination)
            print("File copied successfully.")
    except shutil.SameFileError:
        print("Source and destination represents the same file.")
    except IsADirectoryError:
        print("Destination is a directory.")
    except PermissionError:
        print("Permission denied.")
    except:
        print("Error occurred while copying file.")


def rename_folder():
    if os.path.exists(r'C:\temp\FailedTestItemsLogs/'):
        copy_file()
        timestampStr = datetime.now().strftime("_%a_%b_%Y_%H_%M_%S")
        os.rename(r'C:\temp\FailedTestItemsLogs', r'C:\temp\FailedTestItemsLogs'+str(timestampStr))


def get_fail_test_case(str_csv_file_path, str_status=['FAIL','WARNING']):
    columns = defaultdict(list)
    lstFailTestCaes = []
    if os.path.exists(str_csv_file_path):
        with open(str_csv_file_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                for (k, v) in row.items():
                    if k in ['Test Item Name', 'Status']:
                        columns[k].append(v)

        for idx, item in enumerate(columns['Test Item Name']):
            if columns['Status'][idx].upper() in str_status:
                lstFailTestCaes.append(columns['Test Item Name'][idx])
        print(lstFailTestCaes)
        return lstFailTestCaes;
    else:
        print("File Not Found...")


def update_mds_file(lst_fail_test_caes, strMdsFilePath):
    lstTestItem = ['MC_Valid_Login','POS_Valid_Login','Create And Set Retail Profile In Enterprise Setting','ReSet Retail Profile And Enterprise Setting','ReSet Retail Profile And Enterprise Setting By Using Database']
    if os.path.exists(strMdsFilePath):
        xmldoc = minidom.parse(strMdsFilePath)
        itemlist = xmldoc.getElementsByTagName('testItem')
        for s in itemlist:
            if s.attributes['name'].value in lst_fail_test_caes or s.attributes['name'].value in lstTestItem or s.attributes['testMoniker'].value in [None, '']:
                #if('verify_Denomination_Symbol_in_MC_Dutch_Netherlands' is not s.attributes['name'].value):
                s.setAttribute('enabled', 'True')

            else:
                s.setAttribute('enabled', 'False')

        with open(strMdsFilePath, 'w') as f:
            f.write(xmldoc.toxml())
    else:
        print("File Not Found...")


def re_run(strCsvFilePath, strMdsFilePath):
    lstFailTestItem = get_fail_test_case(strCsvFilePath) #Create List Of All Fail And Waarn Test Item.
    update_mds_file(lstFailTestItem, strMdsFilePath) #Update .mds file.
    copy_file()# Copy .csv file into FailedTestItemsLogs Folder
    rename_folder() #Rename FailedTestItemsLogs Folder by FailedTestItemsLogs+Timestamp

re_run(r'D:\AllTestItems656.csv',r'D:\Citixsys_Regression.mds')

#if __name__== "__main__":
#    pass
  #re_run(sys.argv[1],sys.argv[2])