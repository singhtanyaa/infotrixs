#!python3
#weather.py -Print the weather for a location from the command line..
import json, sys, requests
#computer location from command line arguments
if len(sys.argv)<2:
    print("Usage: weather.py location")
    sys.exit()
location = ' '.join(sys.argv[1:])
url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=98ebf1857e28352431092b2f1821f59a"%location
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
data = weatherData['weather']
print("Current weather in %s" % (location))
print(data[0]['main'],"-",data[0]['description'])

temp = weatherData['main']
print("Temperature is:",temp['temp']-273.15,"C")
print()

