import json

with open("JSON1.json","r") as file:
    b = json.load(file)

print(b)