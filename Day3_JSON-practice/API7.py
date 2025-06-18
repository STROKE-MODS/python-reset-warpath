import requests

url = "https://jsonplaceholder.typicode.com/posts"

a = {
    "title": "Data Science",
    "body": "First step to internship",
    "userId": 9
}


d = requests.post(url, json=a)

