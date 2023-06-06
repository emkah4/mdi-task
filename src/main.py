from api.weather_api import WeatherApi
from data.csv_writer import CsvWriter
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    weather_api = WeatherApi(api_key=os.getenv('API_KEY'))
    csv_writer = CsvWriter(file_path='../result-data/weather_data.csv')

    cities = ['Vilnius', 'Kaunas', 'Klaipėda']
    weather_data = weather_api.get_weather_data(cities)
    
    csv_writer.write_data(weather_data)

if __name__ == "__main__":
    main()
