import requests
import json
from datetime import datetime, timedelta
from notify_run import Notify 
import time

# All other variables
notify = Notify()
j = 0
TempDict = {}
heaters = None

# Forever cycle for all the API stuff
while True:
    # Time and date gathering
    now = datetime.now()
    current_hour = now.strftime("%H")
    today = datetime.date(now)
    tomorrow = today + timedelta(6)
    iso_todate = today.isoformat()
    iso_tomordate = tomorrow.isoformat()
    weekday = now.weekday()

    # API params
    url = "https://api.open-meteo.com/v1/forecast"
    body = {
        "latitude" : 50.77,
        "longitude" : 15.06,
        "timezone" : "auto",
        "current_weather" : True,
        "windspeed_unit" : "kn",
        "start_date" : iso_todate,
        "end_date" : iso_tomordate,
        "hourly" : ("temperature_2m")

    }

    # Status code handling
    response = requests.get(url, params=body)
    if response.status_code == 200:
        print("Succes!\n")
    else:
        print("Something went wrong! ("+str(response.status_code)+")")
        quit()

    #Simplier Dictionaries from the response
    ResponseDict = response.json()
    CurrentDict = ResponseDict["current_weather"]
    WeatherTime = CurrentDict["time"]
    HourlyDict = ResponseDict["hourly"]
    TimeList = HourlyDict["time"]
    TemperatrureList = HourlyDict["temperature_2m"]

    # Current weather printing
    print("Time: "+WeatherTime[-5:])
    print("Current temperature: "+str(CurrentDict["temperature"])+" °C")
    print("Current windspeed: "+str(CurrentDict["windspeed"])+" kts")
    print("Current wind direction: "+str(CurrentDict["winddirection"])+"°")
    notify.send("Current weather \nTime: "+WeatherTime[-5:]+"\nCurrent temperature: "+str(CurrentDict["temperature"])+" °C"+"\nCurrent windspeed: "+str(CurrentDict["windspeed"])+" kts"+"Current wind direction: "+str(CurrentDict["winddirection"])+"°")

    # Forecast handling
    for i in TimeList:
        TempDict[i] = float(TemperatrureList[j])
        j = j+1

    for k in TempDict.values():
        if k <= 0:
            heaters = True
        else:
            heaters = False

    # Notify.run notification + CML print
    if weekday == 6 and current_hour == "18":
        if heaters:
            print("Turn on the heaters")
            notify.send('Okap heater \nTurn on the heaters') 
        else:
            print("No need to run the heaters")
            notify.send('Okap heater \nNo need to run the heaters')

    time.sleep(3600)