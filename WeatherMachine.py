import requests #The requests module in Python is used to make HTTP requests in a simple and human-friendly way
import json
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 110)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Dictionary to map wind direction abbreviations to full names
wind_directions = {
    "N": "North",
    "NNE": "North-Northeast",
    "NE": "Northeast",
    "ENE": "East-Northeast",
    "E": "East",
    "ESE": "East-Southeast",
    "SE": "Southeast",
    "SSE": "South-Southeast",
    "S": "South",
    "SSW": "South-Southwest",
    "SW": "Southwest",
    "WSW": "West-Southwest",
    "W": "West",
    "WNW": "West-Northwest",
    "NW": "Northwest",
    "NNW": "North-Northwest"
}



city= input("Please type the location name:\n")
url=f"https://api.weatherapi.com/v1/current.json?key=a501493ff8224bf091f71828241805&q={city}"
r=requests.get(url) #Sends a GET request to the specified URL.
wdic=json.loads(r.text) #to convert a string into dictionary
temp=wdic["current"]["temp_c"]
condition=wdic["current"]["condition"]["text"]
humidity=wdic["current"]["humidity"]
uv=wdic["current"]["uv"]
wdir=wdic["current"]["wind_dir"]
wsp=wdic["current"]["wind_kph"]

full_wdir = wind_directions.get(wdir, wdir)  # Default to abbreviation if not found

engine.say(f"The current temperature in {city} is {temp},condition is {condition},humidity is {humidity},wind speed is {wsp},wind direction is  {full_wdir} and uv is {uv}")
engine.runAndWait()