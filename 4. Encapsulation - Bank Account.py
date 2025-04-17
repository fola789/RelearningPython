'''
1. Repeat the question to have a clear statement in my own words of what needs to be done(very important)
2. Ask clarifying questions to check any assumptions that you have
3. Think about some example inputs and the corresponding outputs ()
4. Brainstorm multiple solutions e.g fasted code in Big O time, most efficient code from a space complexity, code that you can implement the fastest to find out what optimal means ()
Create a bank account that has capabilities to return the balance, add money to the balance or take money away from the balance

'''

class BankAccount:
    def __init__(self, account_username: str, balance: float) -> None:
        self.account_username = account_username
        self.balance = balance

    def get_balance(self) -> str:
        return f"The current balance of {self.account_username}, is $ {self.balance}"

    def deposit(self, amount) -> str:
        if amount <=0:
            return "Deposit amount must be positive."
        self.balance += amount
        return f" {self.account_username}, has deposited $ {amount} to their balance"

    def withdraw(self, amount) -> str:
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f" {self.account_username}, has withdrew $ {amount} from their balance"


account1 = BankAccount("FolaO", 4123.00)
account2 = BankAccount("JackF", 90000.50)

print(account1.deposit(200))        # FolaO has deposited $200.00 to their balance
print(account1.get_balance())       # The current balance of FolaO is $4323.00

print(account2.withdraw(10000))     # JackF has withdrew $10000.00 from their balance
print(account2.get_balance())       # The current balance of JackF is $80000.50

print(account1.deposit(-200)) # Try to deposit a negative amount
print(account1.withdraw(-200)) # Try to withdraw a negative amount
print(account1.withdraw(6000))