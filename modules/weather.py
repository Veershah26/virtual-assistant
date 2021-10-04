from pyowm.owm import OWM
from pyowm.utils import timestamps
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
location = 'Richmond, US'
# Choose between Celsius or Fahrenheit
temp_type = 'fahrenheit'

owm = OWM(key)
mgr = owm.weather_manager()

# Search for current weather in any location
observation = mgr.weather_at_place(location)
weather= observation.weather

temp = weather.temperature(temp_type) # {'temp': 75.36, 'temp_max': 78.24, 'temp_min': 72.41, 'feels_like': 76.41, 'temp_kf': None}
detail = weather.detailed_status # broken clouds
wind = weather.wind() # {'speed': 2.68, 'deg': 246, 'gust': 5.36}
humidity = weather.humidity # 81
rain = weather.rain # {}
heat_index = weather.heat_index # None
clouds = weather.clouds # 75


# Will it be clear tomorrow at this time in my city/country?
forecast = mgr. forecast_at_place(location, 'daily')
# Returns boolean response
answer = forecast.will_be_clear_at(timestamps.tomorrow()) # False