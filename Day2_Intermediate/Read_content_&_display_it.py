class read:
   def reader(self):
    with open ("your_file_name.txt","r") as file:
        d  = file.read()
        print(f"The data inside the file is  : {d}") #Your data inside the file

d = read()
d.reader()