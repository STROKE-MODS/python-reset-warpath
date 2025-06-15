class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = int(balance)
        print(f"Hello {self.name}!\nYour starting balance is ₹{self.balance}")

    def spend(self, amount):
        amount = int(amount)
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"You spent ₹{amount}. Remaining balance: ₹{self.balance}")

    def deposit(self, amount):
        amount = int(amount)
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")
