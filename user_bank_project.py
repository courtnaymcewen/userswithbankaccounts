class User:
    def __init__(self, username, email_address, account_balance):
        self.username= username
        self.email = email_address
        self.account_balance = account_balance

    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    
    def make_transfer(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        
    def display_account(self):
       print(f'Username: {self.username} , Balance: {self.account_balance}')

new_user = User('Steven Johns','sjohns@gmail.com', 200)
new_user2 = User('Rhonda Watts','rwatts@gmail.com', 300)
new_user3 = User('Stephaine Bainbridge','sbainbridge@gmail.com', 300)
 
print (new_user.username) 
print (new_user.account_balance)

print (new_user2.username) 
print (new_user2.account_balance)

print (new_user3.username) 
print (new_user3.account_balance)

new_user.make_deposit(200)
new_user.make_deposit(100)
new_user.make_deposit(250)
new_user.make_withdrawl(300)
new_user.display_account()


new_user2.make_deposit(200)
new_user2.make_deposit(100)
new_user2.make_withdrawl(50)
new_user2.make_withdrawl(300)
new_user2.display_account()


new_user3.make_deposit(800)
new_user3.make_withdrawl(100)
new_user3.make_withdrawl(500)
new_user3.make_withdrawl(200)
new_user3.display_account()

new_user.make_transfer(new_user2, 50)
new_user.display_account()
new_user2.display_account()