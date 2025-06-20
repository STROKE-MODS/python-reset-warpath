import json
import requests

def func():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()
    i=0
    for line in data:
        if "dolor" in line['title'].lower():
            print(line['title'])
            i +=1
    print(f"The number of title containing dolo is {i}")     
func()
        
    

    
    