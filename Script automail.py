#!/usr/bin/python3
import smtplib, sys
from email.mime.text import MIMEText
from email.header import Header
from pushbullet import Pushbullet

frm='marcus.luetolf@bluewin.ch'
to='marcus.luetolf@bluewin.ch'
smtpHost='smtpauths.bluewin.ch'
smtpPort=465

smtpUser='marcus.luetolf'
smtpPassword='gcbadRagaz119'
subj='von RPi SeemoevBucht'
msg='RPi SeemoeveBucht eingeschaltet'

api_key = 'o.A9yPjSAqbRnUk3QKEHOo71i4WDf7itmV'
phone_number="41797438094"
pb=Pushbullet(api_key)

mime=MIMEText(msg, 'plain', 'utf-8')
mime['From']=frm
mime['To']=to
mime['Subject']=Header(subj, 'utf-8')

smtp=smtplib.SMTP_SSL(smtpHost, smtpPort)
smtp.login(smtpUser, smtpPassword)
smtp.sendmail(frm, to, mime.as_string())
smtp.quit()

try:
    device=pb.devices[0]
    device=pb.push_sms(device, phone_number, 'RPi SeemoeveBucht eingeschaltet')
except ConnectionResetError:
    print('Ende Program')
    sys.exit()
