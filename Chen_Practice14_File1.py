import csv

filename = "ateez.csv" 

songs = [
    {"Song": "Thanxx", "Year": 2020},
    {"Song": "Deja vu", "Year": 2021},
    {"Song": "Halazia", "Year": 2022},
    {"Song": "Bouncy", "Year": 2023},
    {"Song": "Work", "Year": 2024}
]

with open(filename, mode='w', newline='') as file:
    fieldnames = ["Song", "Year"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(songs)

with open(filename, mode='r') as file:
    reader = csv.DictReader(file)
    print(f"Filename: {filename}")
    for row in reader:
        print(row)
