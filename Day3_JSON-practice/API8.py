import requests

d = "https://jsonplaceholder.typicode.com/posts/3"

x ={
  "title": "Gym Day",
  "body": "Leg day baby",
  "userId": 2
}



b = requests.put(d,json = x)

print(b.status_code)