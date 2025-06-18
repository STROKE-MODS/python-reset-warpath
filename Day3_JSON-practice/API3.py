import requests

d = requests.get("https://jsonplaceholder.typicode.com/posts")

c = d.json()

for line in c:
    if line['userId'] ==1:
        print(f"{line['title']}")