import csv
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data/sitka_weather_07-2018_simple.csv')
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)