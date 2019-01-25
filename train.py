import urllib.request, json
import speech
def getpnr():
	with urllib.request.urlopen("https://api.railwayapi.com/v2/pnr-status/pnr/4244155114/apikey/4khkpfnhvz/") as url:
		data = json.loads(url.read().decode())
		cs=data['passengers'][0]
		speech.say(str(cs['current_status']).replace('/',' '))