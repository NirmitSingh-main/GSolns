from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_KEY = os.getenv("Weather_API_KEY")

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        return "Unknown", 0
    
    data = response.json()
    
    weather = data['weather'][0]['main']
    temp = data['main']['temp']
    
    return weather, temp