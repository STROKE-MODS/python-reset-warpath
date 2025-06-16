from datetime import datetime

class books:

    def __init__(self):
        self.books = ["Angel next door spoils me rotten" , "Bunny girl senpai" , "I want to eat your pancreas" , "Classroom of the elites"]
        print(f"Books available : {self.books}")

    def name(self):
        try:
            self.c = input("Enter your name : ")
            if self.c.isnumeric():
                raise ValueError

        except ValueError:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Please write your name.")
            with open("Error.txt", "a") as file:
                file.write(f"ValueError had occured on {time}")


        except Exception as e:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("An error occured")
            with open("Error.txt", "a") as file:
                file.write(f"{e} on :{time}")
    def issue(self):
        try:
            time =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.d = input("Enter the book you want : ")
            with open("Record.txt", "a") as file:
                file.write(f"\n Name: {self.c} \n\tName of book: {self.d} \t Status: Issued \t Time: {time}")
            if self.d not in self.books:
                raise FileNotFoundError
            if self.d.isnumeric():
                raise ValueError
        except FileNotFoundError:
            time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            print("Sorry that book is not available.")
        except ValueError:
            time =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Write in alphabets.")
            with open("Error.txt" , "a") as file:
                file.write(f"ValueError occured on {time}\n")
        except Exception as e:
            time= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("An unknow error occured.\n")
            with open("Error.txt", "a") as file:
                file.write(f"{e} had occured on {time}.\n")

    def return_book(self):
        try: 
            time =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.x = input("Enter the book you want to return: ")
            with open("Record.txt", "a") as file:
                file.write(f"\n Name: {self.c} \n\tName of book: {self.x} \t Status: Returned \t Time: {time}")
                if self.x.isnumeric():
                    raise ValueError
        except ValueError:
            time =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Write in alphabets.")
            with open("Error.txt" , "a") as file:
                file.write(f"ValueError occured on {time}")
        except Exception as e:
            time= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("An unknow error occured.")
            with open("Error.txt", "a") as file:
                file.write(f"{e} had occured on {time}.")
    def add_book(self):
        try:
            time =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.y = input("Enter the book you want to add in our library : ")
            if self.y not in self.books:
                self.books.append(self.y)
                with open("Record.txt", "a") as file:
                    file.write(f"\n Name: {self.c} \n\tName of book: {self.y} \t Status: Added \t Time: {time}")
            else:
                    print("This book is already in our store. \n Sorry")
            if self.y.isnumeric():
                raise ValueError
        except ValueError:
            time =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Write in alphabets.")
            with open("Error.txt" , "a") as file:
                file.write(f"ValueError occured on {time}")
        except Exception as e:
            time= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("An unknow error occured.")
            with open("Error.txt", "a") as file:
                file.write(f"{e} had occured on {time}.")
    def view_log(self):
        with open("Record.txt" , "r") as file:
            self.d = file.read()
        print(self.d)
lib = books()
while True:
    z = input("Hello! \n Welcome to our library \n What do you want us to do for you? \n (Book_Issue / Return Book / Add book / View log / Exit ) ")
    if z.lower() == "book_issue":
        lib.name()
        lib.issue()
    elif z.lower() =="return_book":
        lib.name()
        lib.return_book()
    elif z.lower() =="add_book":
        lib.name()
        lib.add_book()
    elif z.lower()=="view_log":
        lib.view_log()
    c= input("Do you want to do anything else: (Yes/No)")
    if c.lower() =="no":
        break
    else:
        print("Invalid Option")


