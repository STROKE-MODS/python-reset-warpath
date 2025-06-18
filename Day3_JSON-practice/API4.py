import requests

d = requests.get("https://jsonplaceholder.typicode.com/comments")

c = d.json()

for lines in c:
    if lines['postId'] ==3:
        print(f"{lines['name']} have email: {lines['email']}")