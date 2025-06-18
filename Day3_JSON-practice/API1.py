import requests
import json

b = requests.get("https://jsonplaceholder.typicode.com/posts")
c = b.json()

print(json.dumps(c, indent=4))