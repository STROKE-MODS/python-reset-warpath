import requests

url = "https://jsonplaceholder.typicode.com/posts/7"

d = requests.delete(url)

print(d.status_code)

