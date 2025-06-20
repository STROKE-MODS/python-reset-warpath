import csv

with open("gym_attendance.csv","w") as file:
   b =  csv.writer(file)
   b.writerow({"Name","Date","Exercise","Duration"})
   b.writerow({"Himanshu","19th of June","Bicep+forearm","1hour30min"})
   
with open("gym_attendance.csv","a") as file:
    b = csv.writer(file)
    b.writerow({"Abhishek","19th of June","Legs","1hour"})