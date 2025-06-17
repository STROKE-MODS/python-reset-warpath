from datetime import datetime
class student:
    def add_student(self):
        try:
            d = input("Enter the name of the student :")
            x = int(input("Enter the student roll number :"))
            print("Student added successfully!!")
            with open("Record.txt", "a") as file:
                file.write(f"\n Name :{d} \t\t Roll No.: {x}")
            if d.isnumeric():
                raise ValueError
        except ValueError:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Please write the correct student name.")
            with open("Error.txt", "a") as file:
                file.write(f"\nValue error has occured on {time}")
        except Exception as e:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("An unknown error has occured.")
            with open("Error.txt", "a") as file:
                file.write(f"\n{e} has occured on {time}")
    def remove_student(self):
        try:
            z = int(input("Enter the student roll number you want to remove: "))
            if z == 0:
                raise NameError
            found = False
            with open("Record.txt", "r") as file:
                lines = file.readlines()
            with open("Record.txt", "w") as file:
                for line in lines:
                        if f"Roll No.: {z}" not in line:
                            file.write(line)
                        else:
                            found = True
            if found:
                print(f"Student removed successfully!")
            else: 
                print(f"No student having roll no. {z} is found.")
        except ValueError:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Enter an Number.")
            with open("Error.txt", "a") as file:
                file.write(f"\nValueError has occured on {time}")
        except NameError:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("No student have roll number zero please write correct roll number.")
            with open("Error.txt", "a") as file:
                file.write(f"\nNameerror has occured on {time}")
        except Exception as e:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("An unknown error has occured.")
            with open("Error.txt", "a") as file:
                file.write(f"\n{e} has occured on {time}")
    def view_log(self):
        try:
            with open("Record.txt", "r") as file:
                c = file.read()
                print(c)
        except Exception as e:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("An unkown error has occured.")
            with open("Error.txt", "a") as file:
                file.write(f"\n{e} has occured on {time}")
    def search(self):
        try:
            m = int(input("Enter the student Roll Number you want to find :"))
            found  = False
            with open("Record.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if (f"Roll No.: {m}" in line):
                        print(line)
                        found = True
            if not found:
                print(f"No Student having Roll no. {m} is found.")
        except ValueError:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Enter the correct value.")
            with open("Error.txt", "a") as file:
                file.write(f"\n ValueError has occured on {time}")
        except Exception as e:
            print("An unknown error has occurred.")
            with open("Error.txt", "a") as file:
                file.write(f"\n {e} has occured on {time}")


            


hello = student()
while True:
    b = input("Enter the work you want to do : \n\t\t(new_admission/remove_student/search_student/view_log/end)")
    if b.lower()=="new_admission":
        hello.add_student()
        z = input("Want to continue? : (Yes/No)")
        if z.lower()=="no":
            print("Thanks for using us")
            break

    if b.lower()=="remove_student":
        hello.remove_student()
        z = input("Want to continue? : (Yes/No)")
        if z.lower()=="no":
            print("Thanks for using us")
            break
    if b.lower()=="search_student":
        hello.search()
        z = input("Want to continue? : (Yes/No)")
        if z.lower()=="no":
            print("Thanks for using us")
            break
    if b.lower()=="view_log":
        hello.view_log()
        z = input("Want to continue? : (Yes/No)")
        if z.lower()=="no":
            print("Thanks for using us")
            break
    if b.lower()=="end":
        print("Thanks for using us")
        break
    
        

    
