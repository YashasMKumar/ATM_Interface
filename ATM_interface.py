import random
import sys

class ATM():
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available balance: Rs.{self.balance}\n")

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Rs.", self.balance)
        print()
        self.transactions.append(f"Deposit: +Rs.{self.amount}")

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is Rs.{self.balance} only.")
            print("Try with a lesser amount than the balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"Nu.{amount} withdrawal successful!")
            print("Current account balance: Rs.", self.balance)
            print()
            self.transactions.append(f"Withdrawal: -Rs.{self.amount}")

    def check_balance(self):
        print("Available balance: Rs.", self.balance)
        print()

    def display_transaction_history(self):
        print("\n----------TRANSACTION HISTORY----------")
        for transaction in self.transactions:
            print(transaction)
        print()

    def transaction(self):
        print("""
            TRANSACTION 

            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Transaction History
            6. Exit

        """)

        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4, 5, or 6: "))
            except ValueError:
                print("Error: Enter 1, 2, 3, 4, 5, or 6 only!\n")
                continue
            else:
                if option == 1:
                    self.account_detail()
                elif option == 2:
                    self.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(Nu.): "))
                    self.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw(Nu.): "))
                    self.withdraw(amount)
                elif option == 5:
                    self.display_transaction_history()
                elif option == 6:
                    print(f"""
                Printing receipt..............

                Transaction is now complete.
                Transaction number: {random.randint(10000, 1000000)}
                Account holder: {self.name.upper()}
                Account number: {self.account_number}
                Available balance: Rs.{self.balance}

                Thank you!
                """)
                    sys.exit()

print("       WELCOME TO ICICI BANK  ")
print("       CREATE YOUR ACCOUNT ")
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
print("Congratulations! Account created successfully.\n")

atm = ATM(name, account_number)

while True:
    trans = input("Do you want to do any transaction?(y/n): ")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""
   | Thank you!! |
   | Visit again!                     |
        """)
        break
    else:
        print("Wrong command! Enter 'y' for yes and 'n' for NO.\n")
