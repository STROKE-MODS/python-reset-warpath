import csv

def city_finder(city):
    with open("6.csv","r") as file:
        b = csv.reader(file)
        next(b)
        found= False
        for i in b:
            if i[0]==city:
                print(f"{i[0]} is in {i[1]} ")
                found = True
            if not found:
                print("City had not been found.")

city_finder("Jaipur")