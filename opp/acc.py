class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    
    def debit(self,amt):
        self.balance-=amt
        print(f'You have debited  : ${amt}')
        
    def credit(self,amt):
        self.balance+=amt
        print(f'You have debited  : ${amt}')


    def check(self):
        print(f'Your balance is : ${self.balance}')


c1=Account(balance=10000,account_no=123)
c1.check()
c1.debit(5000)
c1.check()
c1.credit(2000)
c1.check()