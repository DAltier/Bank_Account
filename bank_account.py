class BankAccount:
    def __init__(self, int_rate, balance) :
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount) :
        self.balance += amount
        return self

    def withdraw(self, amount) :
        self.balance -= amount
        return self
    
    def display_account_info(self) :
        print("Account balance", self.balance)
        return self

    def yield_interest(self) :
        self.balance += self.balance * self.int_rate
        return self

alex = BankAccount(2, 50)
amy = BankAccount(5, 100)

alex.deposit(200).deposit(500).deposit(50).withdraw(100).display_account_info()
amy.deposit(900).deposit(150).withdraw(100).withdraw(75).withdraw(25).withdraw(50).yield_interest().display_account_info()
