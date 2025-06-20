import csv

def func():
    with open("8.csv","r") as file:
        b = csv.reader(file)
        next(b)
        c=-1
        for line in b:
            x = int(line[2])
            if x>c:
                c = x
                topper = line[0]
        print(f"{topper} had got highest in Mathematics.")
                        
func()