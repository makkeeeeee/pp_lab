class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}; The new balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("error balance.")
        else:
            self.balance -= amount
            print(f"quit {amount}. New balance is {self.balance}")


# Test the class
account = BankAccount("Mariya Erzhan", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)