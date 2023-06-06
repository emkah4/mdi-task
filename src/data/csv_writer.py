import csv

class CsvWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_data(self, data):
        with open(self.file_path, mode='w', newline='') as file:

            fieldnames = ['city', 'date', 'min-temp', 'max-temp', 'condition']

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for city, weather in data.items():
                for attributes in weather:
                    writer.writerow({
                        'city': city, 
                        'date': attributes['date'], 
                        'min-temp': attributes['min'],
                        'max-temp': attributes['max'],
                        'condition': attributes['condition'],
                    })
