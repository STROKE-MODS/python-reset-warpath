import csv

def func():
    with open("8.csv","r") as file:
        b = csv.reader(file)
        next(b)
        found = False
        for line in b:
            if int(line[2])>80 and int(line[3])>80:
                print(f"{line[0]} had got {line[2]} in Mathematics and {line[3]} in Physics.")
                found  =True
        if not found:
            print("No student had got more than 80 marks in both subjects")

func()
        