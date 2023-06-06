import requests
from requests.exceptions import JSONDecodeError
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import sys

class WeatherApi:
    def __init__(self, api_key, base_url="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"):
        self.api_key = api_key
        self.base_url = base_url

    def fetch_weather_data(self, city, today):
        try:
            response = requests.get(f"{self.base_url}/{city},LT/2023-01-01/{today}?unitGroup=metric&key={self.api_key}&include=days&elements=datetime,tempmax,tempmin,humidity,conditions")
            return response.json()
        except JSONDecodeError:
            print(f"[429] Failed to parse JSON for {city}. Too many requests.")


    def get_weather_data(self, cities):
        today = datetime.now().strftime('%Y-%m-%d')
        with ThreadPoolExecutor(max_workers=3) as executor:
            data = list(executor.map(self.fetch_weather_data, cities, today))
        return data
