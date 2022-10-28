class AccountError(Exception):
    pass

class Account:
    def __init__(self, accNumber):
        self.__AccNumber = accNumber
        self.__AccBalance = 0

    @property
    def account(self):
        return self.__AccNumber
    
    @account.deleter
    def account(self):
        if (self.__AccBalance > 0):
            raise AccountError ("Account " + self.__AccNumber + " has balance. It can be deleted!")
        else:
            self.balance = 0
            self.__AccNumber = None

    @property
    def balance(self):
        return self.__AccBalance
    
    @balance.setter
    def balance(self, value):
        if abs(value) > 100000:
            print ("Ammount over $100.000")

        if value > 0:
            self.__AccBalance += value
        else:
            if (self.__AccBalance - abs(value) < 0):
                raise  AccountError ("Not possible to set negative balance.")
            else:
                self.__AccBalance -= abs(value)


NewAccount = Account("12345678")   
print (NewAccount.account, NewAccount.balance)

try:
    NewAccount.balance= -200
except AccountError as Err:
    print ("Transaction Error: ", Err)
print (NewAccount.account, NewAccount.balance)

try:
    NewAccount.balance=1000000
except AccountError as Err:
    print ("Transaction Error: ", Err)
print (NewAccount.account, NewAccount.balance)

try:
    del NewAccount.account
except AccountError as Err:
    print ("Account Deletion Error: ", Err)