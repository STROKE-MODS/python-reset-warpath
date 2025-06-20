import csv

def search_city(name):
    with open("3.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        found = False
        for row in reader:
            if row[0] == name:
                print(f"{name} lives in {row[1]}")
                found = True
        if not found:
            print("Name not found.")

search_city("Rohan")
