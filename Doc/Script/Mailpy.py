import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os.path import basename

class Mail:
	def __init__(self):
		Log.Message("Initializing Mail Class");
		
	def SendMail(Sender=None,Recipient=None,Subject=None,Body=None,Attachments=None):
	  AttachmentList = Attachments;
	  try:	
	    with open(Project.Path+"TestRepo\E-Mail Template\MailTemplate.txt", 'r') as MailTemplate:
	      html=MailTemplate.read()
	      
	    msg = MIMEMultipart('alternative')
	    msg['Subject'] = Subject
	    msg['From'] = Sender
	    msg['To'] = Recipient
	    BodyMsg = MIMEText(aqString.Replace(html,"MSG", Body), 'html')
	    if(AttachmentList is not None):
	      for AttachmentFile in AttachmentList:
	        FileName = basename(AttachmentFile)
	        File = open(AttachmentFile, "rb")
	        Attachment = MIMEBase('application', 'octet-stream')
	        Attachment.set_payload((File).read())
	        encoders.encode_base64(Attachment)
	        Attachment.add_header('Content-Disposition', "attachment; filename= %s" % FileName)
	        msg.attach(Attachment)
	        
	    msg.attach(BodyMsg)
	    ObjSMTP = smtplib.SMTP("smtp.corp.seic.com")
	    ObjSMTP.sendmail(Sender, msg["To"].split(","), msg.as_string())
	    ObjSMTP.quit()
	    Log.Message("Successfully sent email");
	  except Exception as e:
	    import sys,os,traceback,inspect
	    exc_type, exc_value, exc_traceback = sys.exc_info()
	    logging.info("","#################################################################") 
	    logging.error("",exc_info=(exc_type, exc_value, exc_traceback)) 
	    logging.info("","#################################################################") 
	    ObjAttributes = Log.CreateNewAttributes()
	    ObjAttributes.Bold = True
	    ObjAttributes.BackColor = clRed
	    ObjAttributes.FontColor = clYellow
	    Log.Error(traceback.format_exc())

	  	  