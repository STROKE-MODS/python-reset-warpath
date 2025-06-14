def func():
    b = int(input("Enter the number:"))
    
    for i in range(2,b):
        if (b%i==0):
            print("The number is not prime")
            break
    else:
            print("The number is prime")

func()