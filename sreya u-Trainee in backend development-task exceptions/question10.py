"""10.Write a Python program that simulates a banking system.
Implement a class called BankAccount with methods to initialize an account with a starting balance, withdraw funds,
and handle a custom exception called NegativeBalanceError when the account balance goes below zero."""

class NegativeBalanceError(Exception):
    pass

class BankAccount:

    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise NegativeBalanceError("Insufficient funds. Cannot withdraw more than the available balance.")
        self.balance -= amount


try:
    initial_balance = int(input("Enter initial balance: ")) 
    account = BankAccount(initial_balance)  
    print("Initial balance:", account.balance)
    
    withdraw_amount = int(input("Enter the amount to withdraw: ")) 
    account.withdraw(withdraw_amount) 
    
    balance_amount=initial_balance - withdraw_amount
    print("balance amount after withdraw is :",balance_amount)
except NegativeBalanceError as e:
    print("Error:", e)

