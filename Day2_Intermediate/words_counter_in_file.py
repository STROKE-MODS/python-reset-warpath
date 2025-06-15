class counter:
    def file(self):
        with open("file.txt" , "w") as file:
            self.d = file.write("Hello World")
        
        with open("file.txt" ,"r") as file:
            y = file.read()
            self.x = len(y.split())
            print(f"Number of words are : {self.x}")

d = counter()
d.file()