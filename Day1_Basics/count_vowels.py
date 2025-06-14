def count_vowels():
    vowels = ["a","e","i","o","u"]
    d = input("Enter the Statement: ")
    count = 0
    for n in d:
        if n.lower() in vowels:
                count +=1       
    print(f"Number of vowels in the statement are :{count} ")
count_vowels()