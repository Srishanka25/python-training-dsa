class Bank_account:
    def __init__(self):
        self.account_number=input("enter account number") 
        self.balance=float(input("enter the balance"))
        self.date_of_opening=input("enter date_of_opening")
        self.cust_name=input("enter name of the customer")
    def deposit(self,amount):
        self.balance+=amount
        print(amount,"is deposited successfully")
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print(amount,"is withdrawn successfully")
    def check_balance(self):
        print("your balance is",self.balance)
obj1=Bank_account()
obj1.deposit(2000)
obj1.withdraw(245)
obj1.check_balance()

    
        

