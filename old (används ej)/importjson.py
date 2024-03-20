import json

with open("persons.json") as f:
    persons = json.load(f)
    print(persons)
