import requests
import json
from datetime import datetime

print(datetime.now())


url = "https://api.open-meteo.com/v1/forecast"
body = {
    "latitude" : 50.77,
    "longitude" : 15.06,
    "timezone" : "auto",
    "current_weather" : True,
    "windspeed_unit" : "kn",
    "start_date" : "2022-12-28",
    "end_date" : "2022-12-30"

}


response = requests.get(url, params=body)
if response.status_code == 200:
    print("Succes!\n")
else:
    print("Something went wrong! ("+str(response.status_code)+")")
    quit()

ResponseDict = response.json()
CurrentDict = ResponseDict["current_weather"]
WeatherTime = CurrentDict["time"]
print("Time: "+WeatherTime[-5:])
print("Current temperature: "+str(CurrentDict["temperature"])+" °C")
print("Current windspeed: "+str(CurrentDict["windspeed"])+" kts")
print("Current wind direction: "+str(CurrentDict["winddirection"])+"°")

{'latitude': 50.78, 'longitude': 15.059999, 'generationtime_ms': 0.9119510650634766, 'utc_offset_seconds': 3600, 'timezone': 'Europe/Prague', 'timezone_abbreviation': 'CET', 'elevation': 382.0, 'current_weather': {'temperature': 1.0, 'windspeed': 17.3, 'winddirection': 138.0, 'weathercode': 3, 'time': '2022-12-28T11:00'}}