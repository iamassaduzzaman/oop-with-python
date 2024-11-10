# read only --> you can not set the value. value can not be changed
# getter --> get a value of a property through a method. most of the time, you will get the value of a private attribute
# setter --> set a value of a property through a method. most of the time, you will set the value of a private property

class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money
    
    @property
    def age(self):
        return self._age
    
    # getter
    @property
    def salary(self):
        return self.__money
    
    # setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            return 'salary can not be negative'
        self.__money += value

samsung = User('kopa', 21, 12000)
# print(samsung.__money)
# print((samsung.age()))
print(samsung.age)
print(samsung.salary)
samsung.salary = 4500
print(samsung.salary)


    
