import csv

def func():
    with open("7.csv","r") as file:
        b = csv.reader(file)
        next(b)
        found  =False
        for line in b:
            if int(line[2])>70:
                print(f"{line[0]} had got {line[2]} in Maths")
                found = True
        if not found:
            print("No student had got more than 70 in Mathematics.")

func()