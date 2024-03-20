import csv

with open ("persons.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)