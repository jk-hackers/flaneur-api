# -*- coding: utf-8 -*-
import requests
import os

def lookup_location(geo):
    url = "https://geoapi.qweather.com/v2/city/lookup?location={}&key={}".format(geo, os.getenv("WEATHER_KEY"))
    return requests.get(url).json()

def get_weather(location):
    url = "https://devapi.qweather.com/v7/weather/now?location={}&key={}".format(location, os.getenv("WEATHER_KEY"))
    return requests.get(url).json()
