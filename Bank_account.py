import datetime
history = {}


class Account:
    def __init__(self):
        self.pin = 1234
        self.balance = 0

    def checkcode(self, value):
        return self.pin == value

    def checkbalance(self):
        print('current balance is', str(self.balance), 'rs.')

    def checktransaction(self):
        print('previous transactions: ')
        for item in sorted(history):
            print(item, str(history[item]), 'rs')

    def withdraw(self, pin, value):
        if self.checkcode(pin):
            if value <= self.balance:
                currentTime = datetime.datetime.now()
                history[str(currentTime)] = -value
                self.balance -= value
                print('Successfully withdrawn ', str(
                    value), 'rs from your account.')
            else:
                print('Not enough balance.')
        else:
            print('Wrong pin code. Try again.')

    def deposit(self, pin, value):
        if self.checkcode(pin):
            self.balance += value
            history[str(datetime.datetime.now())], +str(value)
            print('Successfully deposited ', str(
                value), ' rs from your account.')
        else:
            print('Wrong pin code. Try again.')

    def changepin(self, oldvalue, newvalue):
        if self.checkcode(oldvalue):
            self.pin = newvalue
            print("pincode has been successfully changed")
        else:
            print("try again!!")


class CheckingAccount(Account):
    def __init__(self):
        super(CheckingAccount, self).__init__()
        self.balance = 12000


class SavingsAccount(Account):
    def __init__(self):
        super(SavingsAccount, self).__init__()
        self.balance = 5000


class BusinessAccount(Account):
    def __init__(self):
        super(BusinessAccount, self).__init__()
        self.balance = 10000


checksAcc = CheckingAccount()
pin = int(input("enter the pin: "))
if checksAcc.checkcode(int(pin)):
    checksAcc.withdraw(1234, 4000)
    checksAcc.deposit(1234, 22000)
    checksAcc.withdraw(1234, 22000)
    checksAcc.deposit(1234, 24000)
checksAcc.checktransaction()
checksAcc.checkbalance()
myAcc = SavingsAccount()
hisAcc = BusinessAccount()
checksAcc.changepin(1234, 5678)
