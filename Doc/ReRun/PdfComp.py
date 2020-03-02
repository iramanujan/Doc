import cv2
from wand.image import Image as wi
import numpy as np
import glob
import os

lstPreShotFiles = glob.glob("D:\PreShot\*.pdf")
lstPostShotFiles = glob.glob("D:\PostShot\*.pdf")


def convert_pdf_to_image(dictLocation):
    dict = {}
    for pdffileName, pdffile in dictLocation.items():
        pdf = wi(filename=pdffile, resolution=300);
        pdfImage = pdf.convert("jpeg");
        i = 1
        for img in pdfImage.sequence:
            page = wi(image=img)
            strPath = '\\'.join(pdffile.split('\\')[0:-1]) + "\\" + pdffileName + "_" + str(i) + ".jpg"
            dict[pdffileName + "_" + str(i)] = strPath
            page.save(filename=strPath)
            i += 1
    return dict


def get_files(location):
    dict = {}
    for file in location:
        filePath = file
        fileName = os.path.splitext(os.path.basename(file))[0].replace(" ", '')
        dict[fileName] = filePath
    return dict


def compare_image(dictpre,dictpost):
    for k, v in dictpost.items():
        try:
            Original = cv2.imread(dictpre[k])
            Edited = cv2.imread(v)
            diff = cv2.subtract(Original, Edited)
            if np.any(diff):
                path = '\\'.join(v.split('\\')[0:-1]) + "\\Diff_" + k + ".jpg"
                print(path)
                cv2.imwrite(path, diff)
            else:
                print("Hello")
        except:
            print("Fail"+k)

dictpre = convert_pdf_to_image(get_files(lstPreShotFiles));
dictpost = convert_pdf_to_image(get_files(lstPostShotFiles));
compare_image(dictpre, dictpost);
