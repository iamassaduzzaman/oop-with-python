class Calculator:
    brand = 'Casio 991'
    
    def sum(self, a, b):
        return a + b
    
    def mul(self, a, b):
        return a * b
    
    def subtraction(self, a, b):
        return a - b
    
    def div(self, a, b):
        return a / b

calc = Calculator()

print(calc.sum(4, 5))
print(calc.mul(4, 5))
print(calc.subtraction(4, 5))
print(calc.div(40, 5))