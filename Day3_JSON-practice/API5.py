import requests

d = requests.get("https://jsonplaceholder.typicode.com/todos")

b = d.json()

for line in b:
    if line['completed'] == False and line['userId'] == 2:
        print(f"{line['title']}")