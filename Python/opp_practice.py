# Q1
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

book1 = Book("House of Dragon", "Yamin", 500)
book1.display_info()


# Q2
class  Bankaccount:
    def __init__(self , account_holder , balance):
        self.account_holder = account_holder
        self.balance = balance

def deposite(self,amount):
    if amount > 0:
        self.balance += amount
        print(f"Deposited : $ {amount}")

    else:
        print("Ammount Credit Sucessfully")


def withdraw(self ,amount):
    if amount > self.balance:
        print("Insufficient Balance")
    elif amount <= 0:
        print("Withdrwal Must be Positive")
    else:
        self.balance -= amount
        print(f"Withdrawl : $ {amount}")


def display_balance(self):
    print(f"Account Holder : {self.account_holder}")
    print(f"")

        
