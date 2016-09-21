import time
from bs4 import BeautifulSoup
from urllib import urlopen
import requests

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#Add amount of seconds you want scraper to perform
def assignmentScraper(seconds):
    while True:
        #This section is an HTTP Request to see if website has changed
        response = requests.get('url')
        lastModified = response.headers["Last-Modified"]
        currentModification = 'Tue, 20 Sep 2016 23:26:34 GMT'
    
        #This Grabs URL and runs through the Beautiful Soup API
        html = urlopen('url').read()
        soup = BeautifulSoup(html,"lxml")

        #This grabs the specific tag 'li' in this content class
        for assignemnts in soup.find('div',{'class':"content"}).findAll('li'):
            toDo = assignemnts.get_text()
    
        if currentModification != lastModified:
            #this updates current mod and then notifies user
            currentModification = lastModified
            sendEmailWithText('email')  
        time.sleep(seconds)

#Add Add the email you want to send to
def sendEmailWithText(to):
    
    
    msg = MIMEMultipart()
    content = MIMEText("A New Assignment Has Been Posted: " + toDo )
    msg.attach(content)
    
    
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('email','password')
    mail.sendmail(to,to,msg.as_string())
    mail.close()
