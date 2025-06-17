import json

with open("JSON3.json", "r") as file:
    a = json.load(file)
with open("JSON2.json", "r") as file:
    b = json.load(file)

a.update(b)

with open("JSON2.json", "w") as file:
    json.dump(a ,file, indent=4)