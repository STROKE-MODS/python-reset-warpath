d = input("Enter the file name : ")

with open(f"{d}.txt" , "w") as file:
    d = "Your data"
    c = file.write(d)

print(c)

