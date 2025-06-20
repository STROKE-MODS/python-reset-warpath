import csv
def func():
    with open("5.csv","r") as file:
        b = csv.reader(file)
        next(b)
        found = False
        for line in b:
            if  int(line[2])>80:
                print(f"{line[0]} had got {line[2]} in physics.")
                found= True
    if not found:
        print("No student had got more than 80 in physics.")

func()