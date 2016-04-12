class BankAccount:
        def __init__(self):
            self.someValue = ''
            self.accntBal = 0

        def deposit(self, amount):
            newDeposit = int(amount)
            self.accntBal =  self.accntBal + newDeposit


        def withdrawl(self, amount):
            newWithdrawl = int(amount)
            self.accntBal = self.accntBal - newWithdrawl


        def checkBal(self):
            print('Your balance is: ' + str(self.accntBal))

        def transfer(self, amount, account):
            newTransfer = int(amount)
            self.withdrawl(amount)
            account.deposit(amount)


#class Bank

#class ATM

#class Teller

a = BankAccount()
b = BankAccount()
a.deposit(5)
a.withdrawl(4)
a.checkBal()
a.transfer(1000, b)
a.checkBal()
b.checkBal()