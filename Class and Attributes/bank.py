class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_balance = 100
        self.max_withdraw = 10000
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount):
        if amount < self.min_balance:
            print(f'fokira you can not withdraw below {self.min_balance}')
        elif amount > self.max_withdraw:
            print(f'bank fokir hoye jabe. you can not withdraw more than {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'here is your money {amount}')
            print(f'your balance after withdraw: {self.get_balance()}')

brac = Bank(150000)
brac.withdraw(50)
brac.withdraw(500000)
brac.withdraw(5000)
print(brac.get_balance())
