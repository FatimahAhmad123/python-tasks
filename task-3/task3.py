#!/usr/bin/python3
import json

# Load data from the input JSON file
with open("Input.json", "r") as file:
    data = json.load(file)

# print(data)

# Create a dictionary to group people by occupation
professions = {}
for person in data:
    occupation = person["occupation"]
    if occupation not in professions:
        professions[occupation] = []
    professions[occupation].append(person)

# Write the grouped data to a new JSON file
with open("output.json", "w") as file:
    json.dump(professions, file, indent=2)

# Print the content of the new file
with open("output.json", "r") as file:
    print(file.read())

print("Grouped data has been written to 'output.json' and printed.")
