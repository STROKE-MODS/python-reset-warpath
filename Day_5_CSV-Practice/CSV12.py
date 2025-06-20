import csv

def func():
    with open("8.csv","r") as file:
        b  =csv.reader(file)
        next(b)
        found = False
        for line in b:
            if 80>int(line[2])>60:
                print(f"{line[0]} had got marks {line[2]}")
                found = True
            if not found:
                print("No student had got marks between 60 and 80.")
func()
        