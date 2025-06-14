def number():
    b = [2,5,6,9,8]
    c=b[0]
    for i in b:
        if i>c:
            c=i
        
    print(f"{c} is the greatest")
        
number()