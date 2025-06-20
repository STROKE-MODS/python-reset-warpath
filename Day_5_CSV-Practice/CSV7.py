import csv

def func():
    with open("7.csv","r") as file:
        b =csv.reader(file)
        next(b)
        found = False
        for line in b:
            if int(line[3])>80:
                print(f"{line[0]} have marks {line[3]} in physics.")
                found = True
        if not found:
            print("No student had got marks more than 80 in physics.")
            
func()
                
    