from currency_converter import CurrencyConverter
def convertor():
	c = CurrencyConverter()
	speech.say("what is the value")
	val=speech.input()
	speech.say("convert from")
	x=speech.input()
	if(x=="dollars" or x=="dollar"):
		x="USD"
	elif(x=="euros"):
		x="EUR"
	elif(x=="rupees"):
		x=="INR"
	elif(x=="pounds"):
		x="GBP"
	elif(x=="yen"):
		x="JPY"
	else:
		speech.say("unknown currency")
		return false
	speech.say("convert to")
	y=speech.input()
	if(y=="dollars" or y=="dollar"):
		y="USD"
	elif(y=="euros"):
		y="EUR"
	elif(x=="rupees"):
		y=="INR"
	elif(y=="pounds"):
		y="GBP"
	elif(y=="yen"):
		y="JPY"
	else:
		speech.say("unknown currency")
		return false
	speech.say("here is your result")
	print(c.convert(val, x , y))
	print(sorted(c.currencies))
if __name__=="__mmain__":
	convertor()