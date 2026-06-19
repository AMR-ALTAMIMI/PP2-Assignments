class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def display_balance(self):
        print(f"Balance: {self.balance}")

account = BankAccount("Ahmed", 1000)

account.deposit(500)

account.display_balance()
