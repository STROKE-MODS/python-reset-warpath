from datetime import datetime

class BankAccount:
    def deposit(self):
        try:
            amount = int(input("Enter amount to be added: ₹"))
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"₹{amount} was credited to your account on {time}")
            with open("transaction.txt", "a") as file:
                file.write(f"[{time}] Deposited: ₹{amount}\n")

        except ValueError:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Use numbers.")
            with open("Error.txt", "a") as file:
                file.write(f"[{time}] ValueError occurred in deposit.\n")

    def withdraw(self):
        try:
            amount = int(input("Enter the amount to be withdrawn: ₹"))
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"₹{amount} was debited from your account on {time}")
            with open("transaction.txt", "a") as file:
                file.write(f"[{time}] Withdrawn: ₹{amount}\n")

        except ValueError:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Use numbers.")
            with open("Error.txt", "a") as file:
                file.write(f"[{time}] ValueError occurred in withdrawal.\n")

    def balance(self):
        print("💰 Balance feature not implemented yet.")

# Main loop
while True:
    account = BankAccount()
    action = input("\nWelcome to BOB\nHow can we help you? (deposit / withdraw / balance): ").lower()

    if action == "deposit":
        account.deposit()
    elif action == "withdraw":
        account.withdraw()
    elif action == "balance":
        account.balance()
    else:
        print("❌ Invalid option. Please choose deposit / withdraw / balance.")

    cont = input("Do you want to continue? (Yes/No): ").lower()
    if cont == "no":
        print("Thank you for using BOB.")
        break
