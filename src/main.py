from api.weather_api import WeatherApi
from data.csv_writer import CsvWriter
from data.database_writer import DatabaseWriter
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    weather_api = WeatherApi(api_key=os.getenv('API_KEY'))

    cities = ['Vilnius', 'Kaunas', 'Klaipėda']

    print("Please choose what you want to do:")
    print("1 - Get current weather")
    print("2 - Retrieve historic data and store to CSV")

    user_choice = input("Enter your choice (1 or 2): ")
    
    if user_choice == '1':
        print("Requesting API...")
        current_weather = weather_api.get_current_weather(cities)
        print("")
        for record in current_weather:
            print(record)

    elif user_choice == '2':
        print("Requesting API...")
        weather_data = weather_api.get_historic_weather_data(cities)
        csv_writer = CsvWriter(file_path='../result-data/weather_data.csv')
        csv_writer.write_data(weather_data)
        print("Data gathered successfully. Writing to CSV...")
        print("Should the app also store the data to a database table?")
        user_choice_csv_db = input("Enter your choice (y or n): ")
        if user_choice_csv_db == 'y':
            print("Writing data to database...")
            connection_string=os.getenv('CON_STRING')
            db_writer = DatabaseWriter(connection_string)
            db_writer.write_data(weather_data)
            print("Task completed successfully.")
        elif user_choice_csv_db == 'n':
            print("Task completed successfully.")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
