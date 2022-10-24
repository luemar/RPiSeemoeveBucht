#!/usr/bin/python3
import smtplib, sys, picamera
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from pushbullet import Pushbullet

frm='my e-mail address'
to='my e-mail address'
smtpHost='my server in address'
smtpPort=465

smtpUser='my first.lastname'
smtpPassword='my password'
subj='von RPi SeemoeveBucht'
msg='Foto von  SeemoeveBucht'
fn='NoIRx.jpg'

camera=picamera.PiCamera()
camera.capture(fn, resize=(640, 480))
camera.close()

mime=MIMEMultipart()
mime['From']=frm
mime['To']=to
mime['Subject']=Header(subj, 'utf-8')

mime.attach(MIMEText(msg, 'plain', 'utf-8'))
f=open(fn, 'rb')
img = MIMEImage(f.read())
f.close()
mime.attach(img)

try:
    smtp=smtplib.SMTP_SSL(smtpHost, smtpPort)
    smtp.login(smtpUser, smtpPassword)
    smtp.sendmail(frm, to, mime.as_string())
    smtp.quit()

except KeyboardInterrupt:
    print('Ende Program')
    sys.exit()
