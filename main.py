import requests
from dotenv import load_dotenv
import os
import json  

def configure():
    load_dotenv()

configure()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv('API_KEY')
CITY = "New Delhi"

if not API_KEY:
    raise ValueError("API_KEY is missing. Check .env file.")

url = f"{BASE_URL}?appid={API_KEY}&q={CITY}"
response = requests.get(url).json()

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Extract weather data
weather_data = {
    "temperature": kelvin_to_celsius(response['main']['temp']),
    "wind": response.get("wind", {}).get("speed", ""),
    "humidity": response['main']['humidity'],
    "city": CITY
}

# Save to a JSON file
with open("weather_data.json", "w") as json_file:
    json.dump(weather_data, json_file, indent=4)
