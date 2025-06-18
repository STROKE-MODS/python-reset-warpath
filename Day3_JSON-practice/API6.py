import requests

d = requests.get("https://jsonplaceholder.typicode.com/albums")

b = d.json()

for lines in b:
    if lines['userId'] ==5:
        print(f"{lines['title']}")