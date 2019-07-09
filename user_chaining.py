class User:
    def __init__(self, username, email_address, account_balance):
        self.username= username
        self.email = email_address
        self.account_balance = account_balance
        

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    
    def make_transfer(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

    def display_account(self):
        print(f'Username: {self.username}, Balance: {self.account_balance}')
        return self

new_user = User('Steven Johns','sjohns@gmail.com', 200)
new_user2 = User('Rhonda Watts','rwatts@gmail.com', 300)
new_user3 = User('Stephaine Bainbridge','sbainbridge@gmail.com', 5000)
 
print (new_user.username) 
print (new_user.account_balance)

print (new_user2.username) 
print (new_user2.account_balance)

print (new_user3.username) 
print (new_user3.account_balance)

new_user.make_deposit(200).make_deposit(100).make_deposit(250).make_withdrawl(300).display_account()

new_user2.make_deposit(200).make_deposit(100).make_withdrawl(50).make_withdrawl(300).display_account()


new_user3.make_deposit(800).make_withdrawl(100).make_withdrawl(500).make_withdrawl(100).display_account()

new_user2.make_transfer(new_user, 8)
new_user.display_account()
new_user2.display_account()       