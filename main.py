import requests
import json
from datetime import datetime, timedelta


today = datetime.date(datetime.now())
tomorrow = today + timedelta(1)
iso_todate = today.isoformat()
iso_tomordate = tomorrow.isoformat()

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


response = requests.get(url, params=body)
if response.status_code == 200:
    print("Succes!\n")
else:
    print("Something went wrong! ("+str(response.status_code)+")")
    quit()

print(response.json())

ResponseDict = response.json()
CurrentDict = ResponseDict["current_weather"]
WeatherTime = CurrentDict["time"]
print("Time: "+WeatherTime[-5:])
print("Current temperature: "+str(CurrentDict["temperature"])+" °C")
print("Current windspeed: "+str(CurrentDict["windspeed"])+" kts")
print("Current wind direction: "+str(CurrentDict["winddirection"])+"°")

{'latitude': 50.78, 'longitude': 15.059999, 'generationtime_ms': 0.9119510650634766, 'utc_offset_seconds': 3600, 'timezone': 'Europe/Prague', 'timezone_abbreviation': 'CET', 'elevation': 382.0, 'current_weather': {'temperature': 1.0, 'windspeed': 17.3, 'winddirection': 138.0, 'weathercode': 3, 'time': '2022-12-28T11:00'}}
{
    'latitude': 50.78, 
    'longitude': 15.059999, 
    'generationtime_ms': 0.8170604705810547, 
    'utc_offset_seconds': 3600, 
    'timezone': 'Europe/Prague', 
    'timezone_abbreviation': 'CET', 
    'elevation': 382.0, 
    'current_weather': {
        'temperature': 7.1, 
        'windspeed': 3.7, 
        'winddirection': 137.0, 
        'weathercode': 3, 
        'time': '2022-12-29T20:00'
    }, 
    'hourly_units': {
        'time': 'iso8601', 
        'temperature_2m': '°C'
    }, 
    'hourly': {
        'time': [
            '2022-12-29T00:00', 
            '2022-12-29T01:00', 
            '2022-12-29T02:00', 
            '2022-12-29T03:00', 
            '2022-12-29T04:00', 
            '2022-12-29T05:00', 
            '2022-12-29T06:00', 
            '2022-12-29T07:00', 
            '2022-12-29T08:00', 
            '2022-12-29T09:00', 
            '2022-12-29T10:00', 
            '2022-12-29T11:00', 
            '2022-12-29T12:00', 
            '2022-12-29T13:00', 
            '2022-12-29T14:00', 
            '2022-12-29T15:00', 
            '2022-12-29T16:00', 
            '2022-12-29T17:00', 
            '2022-12-29T18:00', 
            '2022-12-29T19:00', 
            '2022-12-29T20:00', 
            '2022-12-29T21:00', 
            '2022-12-29T22:00', 
            '2022-12-29T23:00', 
            '2022-12-30T00:00', 
            '2022-12-30T01:00', 
            '2022-12-30T02:00', 
            '2022-12-30T03:00', 
            '2022-12-30T04:00', 
            '2022-12-30T05:00', 
            '2022-12-30T06:00', 
            '2022-12-30T07:00', 
            '2022-12-30T08:00', 
            '2022-12-30T09:00', 
            '2022-12-30T10:00', 
            '2022-12-30T11:00', 
            '2022-12-30T12:00', 
            '2022-12-30T13:00', 
            '2022-12-30T14:00', 
            '2022-12-30T15:00', 
            '2022-12-30T16:00', 
            '2022-12-30T17:00', 
            '2022-12-30T18:00', 
            '2022-12-30T19:00', 
            '2022-12-30T20:00', 
            '2022-12-30T21:00', 
            '2022-12-30T22:00', 
            '2022-12-30T23:00'
            ], 
        'temperature_2m': [
            3.8, 
            3.6, 
            3.4, 
            3.7, 
            4.1, 4.1, 4.1, 4.2, 4.1, 4.1, 4.9, 5.9, 6.6, 7.4, 7.3, 7.1, 6.8, 6.9, 7.8, 7.6, 7.1, 6.5, 6.4, 6.2, 5.9, 5.6, 5.7, 5.7, 5.6, 5.5, 5.3, 4.6, 4.3, 4.2, 5.0, 5.9, 6.4, 6.7, 6.5, 6.0, 5.3, 4.9, 4.9, 4.8, 4.7, 4.4, 4.4, 4.5]}}