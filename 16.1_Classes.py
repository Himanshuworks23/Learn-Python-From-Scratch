class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = float(balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited amount of Rs{amount} successful, and current account balance is {self.balance}"
        return "Invalid deposit value"

    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
            return f"Withdrawal of amount of Rs {amount} successful, and current account balance is {self.balance}"
        return "Invalid Withdrawal Amount"

    def get_balance(self):
        return f"The current Balance is : {self.balance}"


account1 = BankAccount("123456789", "asghd utqew", "46589")
# account2 = BankAccount("987654321", "cmhve qwuyt", "32487")


print("Hello User, Please select the option from section below:\n"
      "1. Deposit\n"
      "2. Withdraw\n"
      "3. Check Balance\n")


choice = int(input("Enter your choice: "))

if choice in range (1,4):                       # if choice is in the range from 1 to 3
    if choice == 1:
        amt = float(input("Enter the amount you want to deposit: "))
        print(account1.deposit(amt))
    elif choice == 2:
        amt = float(input("Enter the amount you want to deposit: "))
        print(account1.withdraw(amt))
    elif choice == 3:
        print(account1.get_balance())
    else:
        print("Invalid Input")
