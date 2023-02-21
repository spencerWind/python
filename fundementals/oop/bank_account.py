class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        self.overdraftAlert = 'Insufficient funds: Charging a $5 fee'

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount < 0):
            print(self.overdraftAlert)
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f'Balance: {self.balance}')
        print(f'Interest Rate: {self.int_rate}')
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += self.balance * self.int_rate
        return self
    
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_1 = BankAccount(int_rate=0.02, balance=0)
        self.account_2 = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, account, amount):
        if(account == 'account_1'):
            self.account_1.deposit(amount)
        else:
            self.account_2.deposit(amount)
        return self

    def make_withdraw(self, account, amount):
        if(account == 'account_1'):
            self.account_1.withdraw(amount)
        else: self.account_2.withdraw(amount)
        return self

    def display_user_balance(self, account):
        if(account == 'account_1'):
            self.account_1.display_account_info()
        else: self.account_2.display_account_info()
        return self
    
    def transfer_money(self, amount, other_user):
        print('WARNING: funds can only be transfered from "accfount_1')
        self.account_1.withdraw(amount)
        other_user.make_deposit('account_1', amount)


    # TESTS 

Account1 = BankAccount(0.04, 1000)

Account2 = BankAccount(0.025, 23500)

Account1.deposit(150).deposit(73).deposit(127).withdraw(450).display_account_info()

Account2.deposit(200).deposit(700).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

User1 = User('Spencer', 'swind03@gmail.com')
User2 = User('Bill', 'bill@gmail.com')

User1.make_deposit('account_1',300).display_user_balance('account_1')
User2.make_deposit('account_1',500).display_user_balance('account_1')

User1.transfer_money(200, User2)
User1.display_user_balance('account_1')
User2.display_user_balance('account_1')
