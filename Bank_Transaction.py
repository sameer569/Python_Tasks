class Bank_Account:
    Account_Number=0
    def __init__(self, First_Name, Last_Name, Balance=1000):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Balance = Balance
        self.Transactions = []
    Account_Number += 1

    def deposit(self, amount):
        self.Balance += amount
        self.Transactions.append(+amount)
        return amount

    def withdrawal(self, amount):
        if self.Balance-amount > 0 :
            if self.Balance-amount >= 500:
                self.Balance -= amount
                self.Transactions.append(-amount)
                return amount
            else:
                return "please maintain minimum account balance of 500"
        else:
            return "Your Transaction cannot be completed,"

    def Transactions(self):
        if len(self.Transactions) < 1:
            return None
        else:
            return self.Transactions.pop()

    def Full_Name(self):
        return "{} {}".format(self.First_Name, self.Last_Name)



cus1=Bank_Account("Maheboob","Tumkur")
print(cus1.deposit(1000))
print(cus1.withdrawal(2001))
print(cus1.Balance)
print(cus1.Transactions)
print(cus1.Account_Number)