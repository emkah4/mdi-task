import requests
import calendar
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import product

class WeatherApi:
    def __init__(self, api_key, base_url="http://api.weatherapi.com/v1"):
        self.api_key = api_key
        self.base_url = base_url

    def fetch_historic_weather_data(self, value, city):
        """Fetches historic weather data from the API"""
        try:
            response = requests.get(f"{self.base_url}/history.json?key={self.api_key}&q={city}&dt=2023-{value[0]}-01&end_dt=2023-{value[0]}-{value[1]}")
            return response.json()
        except Exception as e:
            print(f"Error occured: {str(e)}")
    
    def fetch_current_weather(self, city):
        """Fetches current weather from the API"""
        try:
            response = requests.get(f"{self.base_url}/current.json?key={self.api_key}&q={city}")
            return response.json()
        except Exception as e:
            print(f"Error occured: {str(e)}")
    
    def filter_historic_data(self, data):
        """Filters and formats the historic data returned by the API"""
        data_dict = {}
        for record in data:
            city = record['location']['name']
            city_data = [
                {
                    'date': day['date'],
                    'min': day['day']['mintemp_c'],
                    'max': day['day']['maxtemp_c'],
                    'condition': day['day']['condition']['text']
                }
                for day in record['forecast']['forecastday']
            ]
            data_dict[city] = city_data
        return data_dict
    
    def filter_current_weather(self, data):
        """Filters and formats the current weather returned by the API"""
        city_weather = [
            f"Weather in {record['location']['name']}: "
            f"Temperature: {record['current']['temp_c']}°C; "
            f"Conditions: {record['current']['condition']['text']}; "
            f"Humidity: {record['current']['humidity']}%"
            for record in data
        ]
        return city_weather
    
    def fetch_and_filter_data(self, city_month_pair):
        """Fetches and filters the data for a city"""
        city, month_value = city_month_pair
        data = self.fetch_historic_weather_data(month_value, city)
        return self.filter_historic_data([data])
    
    def create_final_dict(self, result_data):
        """Collates all the weather data into a single dictionary"""
        final = {}
        for item in result_data:
            for city, data in item.items():
                if city in final:
                    final[city].extend(data)
                else:
                    final[city] = data
        return final

    def get_historic_weather_data(self, cities):
        """Fetches and filters historic weather data for the given cities"""
        current_month = datetime.now().month
        months = [(i + 1, calendar.monthrange(2023, i + 1)[1]) for i in range(current_month)] # array with month and number of days in that month - using weatherapi.com you can only get data for 1 month per 1 request
        city_month_pairs = list(product(cities, months))

        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = [executor.submit(self.fetch_and_filter_data, pair) for pair in city_month_pairs]
            result_data = [future.result() for future in as_completed(futures)]

        return self.create_final_dict(result_data)
    
    def get_current_weather(self, cities):
        """Fetches and filters current weather data for the given cities"""
        with ThreadPoolExecutor(max_workers=3) as executor:
            data = list(executor.map(self.fetch_current_weather, cities))

        return self.filter_current_weather(data)
