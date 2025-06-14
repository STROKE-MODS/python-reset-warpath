def palindrome():
    b = input("Enter a palindrome : ")

    if b==b[::-1]:
        print("The number is palindrome.")
    else:
        print("The number is not palindrome.")
        

palindrome()