class deposit:
    def entry(self):
        self.x = int(input("Enter your amount to be added : "))
        print("Your transaction is completed.")

        with open("transaction.txt", "a") as file:
            file.write(f"\nDeposited : ${self.x} ")    
class withdraw:
    def remove(self):
        self.x = int(input("Enter the amount to be withdrawn : "))
        print("Your transaction is completed")

        with open("transaction.txt", "a") as file:
            file.write(f"\nWithdrawn : ${self.x} ") 
class viewlog:
    def func(self):
        with open("transaction.txt", "r") as file:
            d = file.readlines()
            print(d)
class end:
    def exit(self):
        print("Thank you for using us!!")

while True:
    d = input("Enter the operation you want : (Deposit/Withdraw/viewlog/end)")
    if d.lower()== "deposit":
        x = deposit()
        x.entry()


    elif d.lower()== "withdraw":
        x = withdraw()
        x.remove()
        
    elif d.lower()== "viewlog":
        x = viewlog()
        
    elif d.lower() == "end":
        x = end()
        x.exit()
        break
        
        
