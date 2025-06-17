import json

with open("JSON2.json","r") as file:
    b = json.load(file)

if "Roll"in b:
    del b["Roll"]

with open("JSON2.json","w") as file:
    json.dump(b,file,indent=4)