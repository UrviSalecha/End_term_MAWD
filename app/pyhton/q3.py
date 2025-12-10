class BankAccount():
    def __init__(self,account_number,account_holder,balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance

#deposit(amount)-> increases balance
#withdraw(amount)->decreases balance(not negative)
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return f"Deposited {amount}. New balance is {self.balance}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self,amount):
        if amount>0:
            if amount<=self.balance:
                self.balance-=amount
                return f"Withdrew {amount}. New balance is {self.balance}."
            else:
                return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."
        
        
account1=BankAccount("12000","Urvi",1000)
account2=BankAccount("10000","ABC",500)
print(account1.deposit(500))  
print(account1.withdraw(200)) 
print(account2.deposit(300))  
print(account2.withdraw(800)) 
