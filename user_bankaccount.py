class BankAccount:
    def __init__(self, int_rate, account_balance):
        self.account_balance = account_balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f'Balance: $ {round(self.account_balance, )} ')
        return self

class User:
    def __init__(self, username, email_address):
        self.username = username
        self.email = email_address
        self.account = BankAccount(0.02, 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdrawl(amount)
        return self

    def display_account(self):
       print(f'Username: {self.username} , Balance: {self.account.account_balance}')

new_user = User('Steven Johns', 'sjohns@gmail.com')
new_user2 = User('Rhonda Watts', 'rwatts@gmail.com')

new_user.make_deposit(200).make_deposit(100).make_deposit(250).make_withdrawl(300).display_account()
new_user2.make_deposit(200).make_deposit(100).make_withdrawl(50).make_withdrawl(100).make_withdrawl(60).make_withdrawl(110).display_account()
    # new_user.make_deposit(200).make_deposit(100).make_deposit(250).withdrawl(300).yield_interest().display_account_info()
    # new_user2.make_deposit(200).make_deposit(100).withdrawl(50).withdrawl(100).withdrawl(60).withdrawl(110).yield_interest().display_account_info()
    # def transfer(self, other_user, amount):
    #     self.account_balance -= amount
    #     new_user.account_balance += amount
    #     new_user2.account_balance += amount
    #     return self

# new_user3 = User('Stephaine Bainbridge','sbainbridge@gmail.com', 300)

# print (new_user.username)
# print (new_user.account_balance)

# print (new_user2.username)
# print (new_user2.account_balance)

# print (new_user3.username)
# print (new_user3.account_balance)

# new_user.deposit(200).deposit(100).deposit(250).withdrawl(300).display_account_info()
# new_user2.deposit(200).deposit(100).withdrawl(50).withdrawl(300).display_account_info()
# new_user3.deposit(800).withdrawl(100).withdrawl(500).withdrawl(200).display_account_info()
# new_user = BankAccount('Steven Johns', .08, 200)
# new_user2 = BankAccount('Rhonda Watts', .06, 300)


# new_user.make_deposit(200).make_deposit(100).make_deposit(250).withdrawl(300).yield_interest().display_account_info()
# new_user2.make_deposit(200).make_deposit(100).withdrawl(50).withdrawl(100).withdrawl(60).withdrawl(110).yield_interest().display_account_info()
