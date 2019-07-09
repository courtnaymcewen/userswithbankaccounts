class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0.00

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f'User: {self.name}, Balance: $ {self.account_balance}')

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


kermit = User("Kermit the Frog", "kermit@muppets.com")
piggy = User("Ms. Piggy", "piggy@muppets.com")
fozzy = User("Fozzy", "fozzy@muppets.com")

kermit.make_deposit(100)
kermit.make_deposit(150)
kermit.make_deposit(200)
kermit.make_withdrawal(120)
kermit.display_user_balance()

fozzy.make_deposit(600)
fozzy.make_withdrawal(60)
fozzy.make_withdrawal(80)
fozzy.make_withdrawal(700)
fozzy.display_user_balance()