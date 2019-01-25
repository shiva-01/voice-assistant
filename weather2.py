import speech
import num
from weather import Weather, Unit
weather = Weather(unit=Unit.CELSIUS)

#place=speech.input()
place='how is weather in hyderabad on first'

def weather():
	location = weather.lookup_by_location(place.split()[4])
	#condition = location.condition()
	#print(condition.text())
	forecasts = location.forecast()
	for forecast in forecasts:
    	#print(forecast.date().split()[0])
    	#print(forecast.text())
    		if str(forecast.date().split()[0]) == str("0"+str(num.text2int(place).split()[6])):
    			print(forecast.text())
    			speech.say("today is" + forecast.text())

if ("weather" or "climate") in place:
	weather()

