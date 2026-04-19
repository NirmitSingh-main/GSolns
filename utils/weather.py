from dotenv import load_dotenv
import requests
import os

load_dotenv()
API_KEY = os.getenv("Weather_API_KEY")

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    try:
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            return "Clear", 25
        
        data = response.json()
        
        weather = data['weather'][0]['main']
        temp = data['main']['temp']
        
        return weather, temp
    
    except:
        return "Clear", 25
    
