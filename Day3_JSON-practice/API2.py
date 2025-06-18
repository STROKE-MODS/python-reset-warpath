import json
import requests

b = requests.get("https://jsonplaceholder.typicode.com/users")
c = b.json()

d = json.dumps(c ,indent = 4)

for lines in c:
    print(f"{lines['name']} have email {lines['email']} ")