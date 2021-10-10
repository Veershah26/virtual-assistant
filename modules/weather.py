from pyowm.owm import OWM
from dotenv import load_dotenv
import os
'''
This module requires that you register for a free account with Open Weather https://openweathermap.org/ and get your own free API key which you can store within the .env file as:
API_KEY = "yourkeyhere123124144345425"
'''
load_dotenv()

# Gets your 'API_KEY' from .env file and stores it as 'key'
key = os.getenv("API_KEY")
# Enter your location here in format 'City, Country'
location =  'London, GB' # 'Banja Luka, BA' 'Ljubljana, SI'
# Choose between Celsius or Fahrenheit
temp_type = 'fahrenheit'
# Choose 'meters_sec', 'miles_hour', 'knots', 'beaufort'
unit='miles_hour'

owm = OWM(key)

mgr = owm.weather_manager()

# Search for current weather in any location
observation = mgr.weather_at_place(location)
weather = observation.weather


def temp ():
  temp = weather.temperature(temp_type)
  return f"The current temperature is {round(temp['temp'])} degrees. Today's high is {round(temp['temp_max'])} degrees and the low is {round(temp['temp_min'])} degrees. "
  # {'temp': 75.36, 'temp_max': 78.24, 'temp_min': 72.41, 'feels_like': 76.41, 'temp_kf': None}

def detail ():
  return f"The sky has {weather.detailed_status}." # broken clouds

def rain ():
  rain = weather.rain
  if rain:
    if '1h' in rain:
      return f"{rain['1h']} millimeters of rain have fallen within the last hour."
    if '3h' in rain:
      return f"{rain['3h']} millimeters of rain have fallen within the last three hours."
  else:
    return "There is no rain in today's forecast."

def pressure ():
  pressure = weather.pressure
  return f"The pressure today is at {pressure['press']} hectopascals."

def wind ():
  wind = weather.wind(unit)
  if unit == "miles_hour":
    wind_unit = "miles per hour"
  if unit == "meters_sec":
    wind_unit = "meters per second"
  if unit == "knots":
    wind_unit == "knots"
  if unit == "beaufort":
    wind_unit == "beauforts"
  if 'speed' in wind:
    return f"Today's wind speed is {round(wind['speed'])} {wind_unit}."
  if 'gust' in wind:
    return f"Today's gust speed is {round(wind['gust'])} {wind_unit}."
  # {'speed': 2.68, 'deg': 246, 'gust': 5.36}

def humidity ():
  return  f"The humidity is {weather.humidity} percent." # 81

def clouds ():
  return f"Cloud coverage is at {weather.clouds} percent." # 75