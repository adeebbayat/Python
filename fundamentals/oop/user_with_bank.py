class BankAccount:
    def __init__(self,int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    
    def deposit(self,amount):
        self.balance += amount
        return self
    
    def withdraw(self,amount):
        if(self.balance > amount):
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if (self.balance > 0):
            self.balance += self.balance*self.int_rate
        return self 
    
    

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02,balance=0)

    def make_deposit(self,amount):
        self.account.deposit(amount)
    
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(f"Balance: ${self.account.balance}")

    def transfer_money(self,amount,other_user):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)


user1 = User("Brad","brad@yahoo.com")
user1.make_deposit(200)
user1.display_user_balance()

user2 = User("Chad","chad@yahoo.com")
user2.make_deposit(200)
user2.display_user_balance()
user1.transfer_money(100,user2)
user1.display_user_balance()
user2.display_user_balance()
