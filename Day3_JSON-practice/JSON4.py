import json

with open("JSON2.json", "r") as file:
    b =json.load(file)

b["Hobby"] = "Gym"

with open("JSON2.json", "w") as file:
    d = json.dump(b , file, indent = 4)