from api.weather_api import WeatherApi
from data.csv_writer import CsvWriter

def main():
    weather_api = WeatherApi(api_key='FZECP3FP3PZX9VT3U67KRJQA4')
    csv_writer = CsvWriter(file_path='result-data/weather_data.csv')

    cities = ['Vilnius', 'Kaunas', 'Klaipėda']
    weather_data = weather_api.get_weather_data(cities)
    for data in weather_data:
        print(data)
    # csv_writer.write_data(weather_data)

if __name__ == "__main__":
    main()
