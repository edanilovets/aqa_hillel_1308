import csv
from pathlib import Path

data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Alice', 25, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]

data_path_file = Path('data/data.csv').absolute()
with open(data_path_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)


with open(data_path_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))