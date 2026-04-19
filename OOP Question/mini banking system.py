'''

Q-2: Bank Class
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

'''

class bankaccount:
    def __init__(self, accountnumber, name, balance):
        self.accountnumber = accountnumber
        self.name = name
        self.balance = balance

    def deposit(self, amount): # deposit the amount
        self.balance += amount
        print(f"deposit is {amount} successfully")

    def withdrawal(self, amount):
        if amount > self.balance: # withdrawl amount
            print(f"insuffcient balance")
        else: 
            self.balance -= amount
            print(f"withdrwal {amount} amount")
    def balance(self):
        fee = 0.05 * self.balance
        self.balance -= fee
        print(f"fees is {fee} applied")

    def display(self): # show the result
        print(f"Account number : {self.accountnumber}")
        print(f"Name : {self.name}")
        print(f"balance : {self.balance}")

new_account = bankaccount(2178514584, "Mandy" , 2800)
new_account.withdrawal(700)
new_account.deposit(1000)

new_account.display()                      