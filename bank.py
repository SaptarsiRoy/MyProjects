#create a banking
class Account():

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    #method for deposit
    def deposit(self, amount):
        self.balance += amount

    # method for withdrawl
    def withdraw(self, amount):

        if(amount > self.balance):
            print("Funds unavailable")
        else:
            print("Withdrawl accepted")
            sel.balance -= amount
