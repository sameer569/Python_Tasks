class Bank_Account:
    def __init__(self,First_Name,Last_Name,Account_Number,Balance=1000):
        self.First_Name=First_Name
        self.Last_Name=Last_Name
        self.Account_Number=Account_Number
        self.Balance=Balance
        self.Transactions=[]

    def deposit(self, amount):
        self.Balance +=amount
        self.Transactions.append(+amount)
        return amount

    def withdrawal(self,amount):
        if self.Balance-amount>0:
            self.Balance -=amount
            self.Transactions.append(-amount)
            return amount
        else:
            return "Your Account does not have sufficient balance"

    def Transactions(self):
        if len(self.Transactions)<1:
            return None
        else:
            return self.Transactions.pop()


cus1=Bank_Account("Maheboob","Tumkur",111222333444)
print(cus1.First_Name)
print(cus1.Account_Number)
cus1.deposit(1000)
print(cus1.Balance)
print(cus1.Transactions)