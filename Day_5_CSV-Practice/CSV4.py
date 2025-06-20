import csv

def student_finder(name):
    with open("4.csv","r") as file:
        b = csv.reader(file)
        found = False
        next(b)
        for line in b:
            if line[0]== name:
                print(f"{name} Class is :{line[1]} and his roll no. is {line[2]}")
                found = True 
    if not found:
        print("No name found.")

student_finder("Himanshu")            
        