import speech
import os
def dimage(name):
	string=["googleimagesdownload --keywords ",name," --limit 2"]
	os.system("".join(string)) 
	speech.say("download sucessful")