import speech
import smtplib
import csv

def getmail(person):
	f=open('people.csv','r')
	r=csv.reader(f)
	for row in r:
		if str(row[0])==person:
			try:
				return row[3]
			except:
				speech.say("sorry but there is no mail id for ",person)
def login(person,message):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("ruthala.shiva512@gmail.com", "Shiva@01")
	server.sendmail("ruthala.shiva512@gmail.com", getmail(person), str(message))
	server.quit()
	speech.say("sent the mail")

def mailtop(person):
	speech.say("What is the message?")	
	while True:
		msg = speech.input()
		print(msg)
		if msg:
			break
		else:
			speech.say("say the message")
			continue
	login(person,msg)
if __name__=="__main__":
	print(getmail('sowri'))