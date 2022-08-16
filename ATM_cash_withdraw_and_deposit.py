
#       this is my first project in python 

class Test:

    def __init__(self,total,withdraw,deposit):
        self.total = total
        self.withdraw = withdraw
        self.deposit = deposit

    def withdrawMoney(self):
        # withdraw = int(input("enter your money withdraw : "))
        print(f"you want to {self.withdraw} rupess to withdraw in your account and your current balance is {self.total}")
        if (self.total>=self.withdraw):
            self.total = self.total-self.withdraw
            print("yout money is withdraw succesfully.")
            print(f"And now your current money is {self.total}")
        else:
            print("insufficent balance.")
    
    def depositMoney(self):
        # deposit= int(input("enter a amout you want to deposit : "))
        print(f"yout total balance is {self.total}")
        print(f"you add {self.deposit} rupess to be deposit in your account and we add this in your account.")
        self.total = self.total+self.deposit
        print(f"and now your total money is : {self.total}")

t = Test(3000,770,500)
t.withdrawMoney()
t.depositMoney()







            #  this is a another code. in this i told that a user can withdraw and doposit money by entring his accout bealance.


'''
class Test:

    def __init__(self,total):
        self.total = total
        # self.withdraw = withdraw
        # self.deposit = deposit

    def withdraw(self):
        withdraw = int(input("enter your money withdraw : "))
        print(f"you want to {withdraw} rupess to withdraw in your account and your total balance is {self.total} ruppes" )
        if (self.total>=withdraw):
            self.total = self.total-withdraw
            print("yout money is withdraw succesfully.")
            print(f"And now your current money is {self.total} ruppes")
        else:
            print("sorry we could not widraw! beacause your withdraw balance is in your aacount is insufficent balance.")

            print('----------------------------------------------------------------------------------------------------------')
    
    def deposit(self):
        deposit= int(input("enter a amout you want to deposit : "))
        print(f"yout total balance is {self.total}")
        print(f"you add {deposit} rupess to be deposit in your account and we add this in your account.")
        self.total = self.total+deposit
        print(f"and now your total money is : {self.total}")

t = Test(300)
t.withdraw()
t.deposit()



'''









