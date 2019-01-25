import os
import smtplib
import speech
import time

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("ruthala.shiva512@gmail.com", "Shiva@01")
mailbox={'chandrahaas':'chandrahaas3@gmail.com','shiva':'ruthala.shiva512@gmail.com',}
#text='mail to shiva'
text=speech.input()
#msg = "message from python....."
speech.say("what is the message")
msg = speech.input()
if text.split()[2] in mailbox.keys():
	server.sendmail("ruthala.shiva512@gmail.com", str(mailbox[text.split()[2]]), str(msg)
	server.quit()