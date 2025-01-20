import requests
from dotenv import load_dotenv
import os

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
    celsius = kelvin - 273.15
    return celsius

# Extract weather data
temp_kelvin = response['main']['temp']
temp_celsius = kelvin_to_celsius(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)

humidity = response['main']['humidity']
description = response['weather'][0]['description']


print(f"Temperature in {CITY}: {temp_celsius:.2f}°C")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}°C")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Weather description: {description}")
