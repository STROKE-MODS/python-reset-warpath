import json
import requests
from datetime import datetime

class students:
    def student_records(self):
            try:
                url = "https://jsonplaceholder.typicode.com/users"
                b = requests.get(url)
                print(b.json())
                try:
                    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open("log.json", "r") as file:
                        y = json.load(file)
                    y["Log had been seen at"]=time
                    with open("log.json","w") as file:
                        json.dump(y,file, indent =4)

                
                except Exception as e:
                    error_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open("Error.json","r") as file:
                        error_file=json.load(file)
                    error_file["Error has occurred"]= error_time
                    with open("Error.json","w") as file:
                        json.dump(error_file, file,indent=4)
            except (FileNotFoundError,json.JSONDecodeError):
                    error_time2 = datetime.now().strftime("%Y:%m:%d %H:%M:%S")
                    print("Error file not found.")
                    with open("Error.json","r") as file:
                            b = json.load(file)
                            b["An error had occured on :"]=error_time2
                    with open("Error.json","w") as file:
                            z = json.dump(b,file,indent=4)
            except Exception as e:
                    error_time3 = datetime.now().strftime("%Y:%m:%d %H:%M:%S")
                    print("Error file not found.")
                    with open("Error.json","r") as file:
                            b = json.load(file)
                            b["An error had occured on :"]=error_time3
                    with open("Error.json","w") as file:
                            z = json.dump(b,file,indent=4)

    def search(self):
        try:
            d = int(input("Enter the Student id : "))
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            url = f"https://jsonplaceholder.typicode.com/users/{d}"
            b = requests.get(url)
            print(b.json())

            try:
                with open("log.json","r") as file:
                    c = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                c = {}

            c["Student Record"] = time_now

            with open("log.json","w") as file:
                json.dump(c, file, indent=4)

        except ValueError:
            print("The Student id should be a number")
            error_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                with open("Error.json","r") as file:
                    x = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                x = {}

            x[f"ValueError on {error_time}"] = "Invalid Student ID input"

            with open("Error.json","w") as file:
                json.dump(x, file, indent=4)

        except Exception as e:
            print("An unknown error has occurred")
            error_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                with open("Error.json","r") as file:
                    x = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                x = {}

            x[f"Exception {e} on {error_time}"] = "Unknown Error"

            with open("Error.json","w") as file:
                json.dump(x, file, indent=4)


    def new_student(self):
        try:
            d = input("Enter the student id: ")
            e = input("Enter the student name: ")
            
            try:
                with open("Student_record.json","r") as file:
                    b= json.load(file)
                    b[d]=e
                with open("Student_record.json","w") as file:
                    json.dump(b,file,indent=4)
                with open("log.json","r") as file:
                    new_Student=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    new = json.load(file)
                new["A new student had been added on :"]= new_Student
                with open("log.json","w") as file:
                    json.dump(new,file,indent=4)
                url = "https://jsonplaceholder.typicode.com/posts"
                url_poster = requests.post(url,json=b)
                print(url_poster.status_code)
            except FileNotFoundError:
                    print("File is not there.")
                    with open("Error.json","r") as file:
                                error=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                y = json.load(file)
                                y["The error had ocurred on :"]=error
                    with open("Error.json","w") as file:
                                json.dump(y,file,indent=4)
        except json.JSONDecodeError:
            b ={}
        except Exception as e:
            error=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("An unknown error has ocurred.")
            with open("Error.json","r") as file:
                x = json.load(file)
            x["The error had ocurred on :"]=error
            with open("Error.json","w") as file:
                json.dump(x,file,indent=4)                

b =students()
print("Hello There!")
while True:
    z = input("What do you want me to do? \n 1.Search for student record? \n 2.Add new student \n 3.Search for a student\n 4.Exit \n:")
    if z.lower()=="student record":
        b.student_records()
        d = input("Do you want to continue? (Yes/No)")
        if d.lower()=="no":
            break
    if z.lower()=="search for student":
        b.search()
        d = input("Do you want to continue? (Yes/No)")
        if d.lower()=="no":
            break
    if z.lower()=="new student":
        b.new_student()
        d = input("Do you want to continue? (Yes/No)")
        if d.lower()=="no":
            break
    if z.lower()=="exit":
        break