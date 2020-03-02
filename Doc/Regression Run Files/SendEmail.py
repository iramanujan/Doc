import csv, smtplib, ssl, email
import base64
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getopt
import sys
import datetime
import socket
 
strFilePath = "C:\\temp\\VersionInfo.txt"
 
def readVersionInfo(listForDebugInfo):
  dictOutput = {}
  if not(os.path.exists(strFilePath)):
   return dictOutput # return if file doesnt exist
  with open(strFilePath, "r") as filePtr :
    list = filePtr.read().split("\n")
    for i in range(0, len(listForDebugInfo)):
     for j in range(0, len(list)):        
        if(listForDebugInfo[i] in list[j]):
          dictOutput[listForDebugInfo[i]] = list[j].split(":")[1]
          break   
  return dictOutput

def getAppVersion():
  strAppPath = "C:\\Program Files (x86)\\CitiXsys\\iVend Retail\\ManagementConsole\\CXSManagementConsole.exe"
  return ""
def getCurrentDate(): 
  now = datetime.datetime.now()
  return str(now.strftime("%Y-%m-%d"))
def sendMail(strLogPath, strFolderPath):
  strAppVersion = getAppVersion()
  from email.mime.text import MIMEText
  from email.mime.multipart import MIMEMultipart
  
  dictVersion = readVersionInfo(["Product Name", "Product Version"])
  if "Product Name" in dictVersion :
    strNameP = dictVersion["Product Name"]
  else :
    strNameP = "Version File not found"
  if "Product Version" in dictVersion :
    strVersion = dictVersion["Product Version"]
  else :
    strVersion = "File not found"	
  sender_email = "CitixsysAutomationTeam@gmail.com"
  #receiver_email = ["praveen.kumar02@nagarro.com"]
  receiver_email = ["anuj.jain03@nagarro.com"]
  password = base64.b64decode(b'Q0FUXzc0MTg1Mjk2Mw==').decode('utf-8')
  
  message = MIMEMultipart("alternative")
  message["Subject"] = "Ivend Version :" + str(strVersion) + " - Regression Result " + getCurrentDate() 
  message["From"] = sender_email
  message["To"] = ", ".join(receiver_email)

  intPassed,intFailed,intWarning,intTotal = 0,0,0,0
  #read the file and get the numbers
  fileName = "C:\\temp\\RegressionResult.csv"
  if os.path.exists(fileName):
    with open(fileName) as csvfile :
      reader = csv.DictReader(csvfile)
      for row in reader:
        intTotal += 1
        if(row['Status'].lower() == "pass"):
          intPassed += 1
        elif(row['Status'].lower() == "fail"):
          intFailed += 1
        elif(row['Status'].lower() == "warning"):
          intWarning += 1	#get the passcount and total count
  strMM = ""	
  if(intTotal != (intPassed + intFailed + intWarning)) :
    strMM = "Total count is not equal to sum of Passed, Failed and Warnings. Kindly check"
  
  
  
  html = """\
	<html>
	<head>
	<style>
	table, th, td {
		border: 1px solid black;
		border-collapse: collapse;
	}
	th, td {     padding: 1px; }
	table {    width: 75%; }
	th, tr {    width: 75%; }
	td#prop {    width: 50%; }sss
	td#val {    width: 50%; }

	table#AutomationResult th	{
		background-color: black;
		color: white;
	}

	table#automationTestExecutionPieChart th	{
		background-color: black;
		color: white;
	}

	</style>
	</head>

	<body>

	Hi All,<br><br>

	Please find below is a summary of Automation Regression Run.<br><br>""" + strMM + """
	
	<table id = "AutomationResult">
		<tr>
			<th colspan="2"> Automation Test Execution Results </th>
		</tr>
		<tr>
			<td id = "prop"> Product Name </td>
			<td id = "val"><font color="purple"> <b> """ + str(strNameP) + """ </b></td>
		</tr>
		<tr>
			<td id = "prop"> Product Version </td>
			<td id = "val"><font color="purple"> <b> """ + str(strVersion) + """ </b></td>
		</tr>		
		<tr>
			<td id = "prop"> Total No. Of Test Executed </td>
			<td id = "val"><font color="purple"> <b> """ + str(intTotal) + """ </b></td>
		</tr>
		<tr>
			<td id = "prop"> Total No. Of Pass Count </td>
			<td id = "val"><font color="green"> <b> """ + str(intPassed) + """ </b></td>
		</tr>
		<tr>
			<td id = "prop"> Total No. Of Warn Count </td>
			<td id = "val"><font color="orange"> <b> """ + str(intWarning) + """ </b></td>
		</tr>
		<tr>
			<td id = "prop"> Total No. Of Fail Count </td>
			<td id = "val"><font color="red"> <b> """ + str(intFailed) + """ </b></td>
		</tr>
	
		<tr>
			<td id = "prop"> Host Machine Name </td>
			<td id = "val"><font color="black"> <b> """ + socket.gethostname() + """ </b></td>
		</tr>
		<tr>
			<td id = "prop"> Path For Full Log File </td>
			<td id = "val"><font color="black"> <b> """ + strLogPath + """ </b></td>
		</tr>
		<tr>
			<td id = "prop"> Path For Test Items Log File (Separate) </td>
			<td id = "val"><font color="black"> <b> """ + strFolderPath + """ </b></td>
		</tr>		
	</table>
	<br>



	Regards,<br>
	CitixSys Automation Team
	</body>
	</html>
	   """
       
#  print(html)
# attach file   if os.path.exists(strFilePath):
  if os.path.exists(fileName):
    with open(fileName, "rb") as attachment:
      part = MIMEBase("application", "octet-stream")
      part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header( "Content-Disposition",f"attachment; fileName= Regression Result.csv")
    message.attach(part)
  if os.path.exists(strFilePath):
    with open(strFilePath, "rb") as attachment:
      part = MIMEBase("application", "octet-stream")
      part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header( "Content-Disposition",f"attachment; fileName= VersionDetails.txt")
    message.attach(part)	
   # Turn these into plain/html MIMEText objects
  part1 = MIMEText(html, "html")
  message.attach(part1)
   # Create secure connection with server and send email
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
       server.login(sender_email, password)
       server.sendmail(
           sender_email, receiver_email, message.as_string()
       )
	   
if __name__== "__main__":	  
  sendMail(sys.argv[1],sys.argv[2])
	
	
	
	
	