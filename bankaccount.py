class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, username, int_rate, account_balance):
        self.username = username
        self.account_balance = account_balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f'Username: {self.username}, Balance: $ {round(self.account_balance, )} ')
        return self

    def yield_interest(self):
        if(self.account_balance > 0):
            self.account_balance *= (1 + self.int_rate)
        else:
            if(self.account_balance <= 0):
                print('Balance is negative') 
        return self


new_user = BankAccount('Steven Johns', .08, 200)
new_user2 = BankAccount('Rhonda Watts', .06, 300)


new_user.deposit(200).deposit(100).deposit(250).withdrawl(300).yield_interest().display_account_info()
new_user2.deposit(200).deposit(100).withdrawl(50).withdrawl(100).withdrawl(60).withdrawl(110).yield_interest().display_account_info()

# 		# your code here#
# class User:
#     def __init__(self, username, email_address, account_balance):
#         self.username= username
#         self.email = email_address
#         self.account_balance = account_balance
#         self.account = bankAccount(int_rate=0.10, balance=0)

#     def deposit(self, amount):
#         self.account_balance += amount
#         return self

#     def withdrawl(self, amount):
#         self.account_balance -= amount
#         return self

#     def transfer(self, other_user, amount):
#         self.account_balance -= amount
#         new_user.account_balance += amount
#         new_user2.account_balance += amount
#         new_user3.account_balance += amount
#         return self
#     def display_account(self):
#         print(f'Username: {self.username} , Balance: {self.account_balance}')
#         return self
# new_user = User('Steven Johns','sjohns@gmail.com', 200)
# new_user2 = User('Rhonda Watts','rwatts@gmail.com', 300)
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
