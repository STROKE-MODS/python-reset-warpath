import csv

def func():
    with open("7.csv","r") as file:
        b =csv.reader(file)
        next(b)
        i=0
        j=0
        for line in b:
            if line[1]=="11th":
                i+=1
            elif line[1]=="12th":
                j+=1
        print(f"Class 12th have {j} students \nClass 11th have {i} students.")
         
func()
            