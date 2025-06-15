class copier:
    def file1(self):
        with open("hello.txt", "r") as file: #put your file name instead of hello.txt
            self.c =file.read()
    def file2(self):
        with open("copied.txt" , "a") as file: #will create or add on the file named as copied having data of your upper file
            file.write(self.c)

d = copier()
d.file1()
d.file2()