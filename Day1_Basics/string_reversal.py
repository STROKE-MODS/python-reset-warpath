#method1
def reverese():
    b = input("Enter the word:")
    c = []
    for i in b:
        c.append(i)
    c.reverse()

    print("".join(c))


#method2
def reverse2():
    b = input("Enter the word:")
    print(b[::-1])
    



reverese()
reverse2()