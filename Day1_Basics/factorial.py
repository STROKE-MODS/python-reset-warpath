def factorial():
    b = int(input("Enter the number for which factorial :"))
    number = 1

    for i in range(1,b+1):
        number*=i
    print(f"The factorial of {b} is : {number}")
        
factorial()

