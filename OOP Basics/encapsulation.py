# encapsulation --> hide details
# access modifier: public, protected, private

class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name # public attribute
        self._branch = 'Banani 11' # protected
        self.__balance = initial_deposit # private
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Fokira taka nai'
    
borolok = Bank('Ami', 100000000)
print(borolok.holder_name)
borolok.deposit(40000)
print(borolok.get_balance())
print(borolok.holder_name)
# print(borolok._branch)
# print(dir(borolok))
print(borolok._Bank__balance) # another way to get balance