"""Q-2: Bank Class
Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details. Give the complete code for the BankAccount class.
Eg. After making above classes and methods, on executing below code:-

newAccount = BankAccount(2178514584, "Mandy" , 2800)

newAccount.Withdrawal(700)

newAccount.Deposit(1000)

newAccount.display()
Output:

Account Number :  2178514584
Account Name :  Mandy
Account Balance :  3100 ₹

"""

class bankaccount:

    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insuffient Balance")
        else:
            print(f"{amount} withdrawl successfully")

    def bankfees(self):
        fees = 0.05 * self.balance
        print(f"Bank fee {fees:.2f}applied ")

    def display(self):
        print('Account number:', self.accountNumber)
        print("Name: ", self.name)
        print("balance: ", self.balance)

newAccount = bankaccount(2178514584, "Mandy" , 2800)

newAccount.withdrawal(200)

newAccount.deposit(1000)

newAccount.display()