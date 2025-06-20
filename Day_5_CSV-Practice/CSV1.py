import csv

with open("sample.csv","a") as file:
    d = csv.writer(file)
    d.writerow(["Rohan","12th","07"])

with open("sample.csv","r") as file:
    x = csv.reader(file)
    for lines in x:
        print(lines)