# PREREQUISITES :
# 1- Have a Gmail Account
# 2- Go to https://myaccount.google.com/security
# 3- Enable Two Step Verification
# 4- Go to the section 'App Passwords'
# 5- Select Messagerie and Computer Windows
# 6- Click on Generate
# 7- Copie the password on orange background and paste it in the 'SMTP_PASSWORD' field in this file

import smtplib
from smtplib import SMTPServerDisconnected
from smtplib import SMTPRecipientsRefused
from smtplib import SMTPDataError
from datetime import date
from time import sleep

from email.mime.text import MIMEText

class Mail():
    def __init__(self):
        self.SMTP_SERVER = "smtp.gmail.com"
        self.SMTP_PORT = 465
        self.today = date.today()

    def sendingmail(self):
        self.overflow = False
        try:
            msg = MIMEText(self.EMAIL_MESSAGE)
            msg['Subject'] = self.EMAIL_SUBJECT
            msg['From'] = self.me
            msg['To'] = self.EMAIL_TO

            self.EMAIL_SUBJECT = f"{self.EMAIL_SUBJECT}"
            self.s.sendmail(self.me, self.EMAIL_TO, msg.as_string())
            print(f"Email successfully sent to {self.EMAIL_TO} !")
            sleep(0.5)
        except SMTPRecipientsRefused:
            with open("./temp/log.txt", 'a') as log:
                log.write(f"{self.EMAIL_TO} (fail) : {self.lastindex+1}\n")
        except SMTPServerDisconnected:
            with open("./logs/reportmailrestart.txt", 'w') as restartmaillog:
                restartmaillog.write("True")
        except SMTPDataError:
            self.overflow = True
            with open("./logs/report.txt", 'a') as scriptlog:
                scriptlog.write(f"{self.today} : Daily limit\n")
                print("\nDaily limit")
            with open("./temp/overflow.txt", 'w') as overflow:
                overflow.write("True")

    def credentials(self):
        self.SMTP_USERNAME = "your@email.com" # change this
        self.SMTP_PASSWORD = "yourpassword" # change this
        self.me = f"Header <{self.SMTP_USERNAME}>" # change this but keep "<{self.SMTP_USERNAME}>"
        self.EMAIL_SUBJECT = "Subject"
        self.EMAIL_MESSAGE = """
Hi I'm Hermes and I love Git !
""" # Change this
        self.s = smtplib.SMTP_SSL(self.SMTP_SERVER, self.SMTP_PORT)
        self.s.ehlo()
        self.s.login(self.SMTP_USERNAME, self.SMTP_PASSWORD)
        print(f"\nLogged in with : '{self.SMTP_USERNAME}'\n")
            
        with open("./temp/liste.txt", 'r') as f:
            liste = f.readline()
            with open(liste, 'r') as listofemails:
                self.lastindex = 0
                with open("./temp/log.txt", 'r') as log:
                    for i in log:
                        pass
                    try:
                        lastline = i                            
                        self.lastindex = int(lastline[lastline.find(":")+1::])+1
                    except UnboundLocalError:
                        self.lastindex = 0
                found = False
                t = 0
                while found == False:
                    for email in listofemails:
                            if t == self.lastindex:
                                self.EMAIL_TO = email
                                if "\n" in self.EMAIL_TO:
                                    self.EMAIL_TO = self.EMAIL_TO[0:-1]
                                self.sendingmail()
                                found = True
                                break
                            t += 1   
        if self.overflow == False:
            with open("./temp/log.txt", 'a') as log:
                log.write(f"{self.EMAIL_TO} : {self.lastindex}\n")

    def main(self):
        with open("./logs/reportmailrestart.txt", 'w') as restartmaillog:
            restartmaillog.write("False")
        with open("./temp/active.txt", 'w') as active:
            active.write("True")
        self.credentials()
        with open("./temp/active.txt", 'w') as active:
            active.write("False")

sendmailall = Mail()        
sendmailall.main()