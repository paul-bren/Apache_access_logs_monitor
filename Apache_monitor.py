import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import glob

l=[]
p=[]
files=[]
o=[]


path = "Z:"
os.chdir(path)
files = glob.glob("localhost_access_log*.txt")
files.sort(key=os.path.getmtime,reverse=True)
files.sort(key=os.path.getctime,reverse=True)
files.append(files)
p=files[0]



with open(p) as f:
    for character, line in enumerate(f, 1):
        found = line.find('HTTP/1.1" 500')
        if found != -1 and found !=0:
            l.append(character)
            if (len(l) > 500000):
                o.append(character)
            else:
                continue
            
if (len(o) >=1):
    smtpServer = "";
    smtpPort = ;
    smtpUsername = "";
    smtpPassword = "";
    toAddress = "";
    fromAddress = "";

    msg = MIMEMultipart()
    msg['From'] = fromAddress
    msg['To'] = toAddress
    msg['Subject'] ="Warning!"
                    
    text = """
This is an automated response. Please check local Apache access logs .
Greater than 500 HTTP 500 errors
"""
    part2 = MIMEText(text, 'plain')
                    
    msg.attach(part2)
    mailServer = smtplib.SMTP(smtpServer , smtpPort)
    mailServer.starttls()
    mailServer.login(smtpUsername , smtpPassword)
    mailServer.sendmail(fromAddress, toAddress.split(",") ,  msg.as_string())
    mailServer.quit()
else:
    pass

