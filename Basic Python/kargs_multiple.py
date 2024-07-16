def full_name(first, last):
    name = f'Full name is: {first} {last}'
    return name

# parameter with serial wise
print(full_name('Jodu', 'Mia')) 

# parameter without serial wise
print(full_name(last = 'Mia', first = 'Jodu'))

'''

*args: take tuple
**args: take dictonary aka key:value pair

'''
def famous_name(first, last, *addition):
    name = f'{first} {last}'
    print('Name: ', name)
    for extra in addition:
        print(extra)

famous_name('Md', 'Assaduzzaman', 'Nilphamari','CS')


def famous_name_(first, last, **addition):
    name = f'{first} {last}'
    print('Name: ', name)
    for key, value in addition.items():
        print(key,': ', value)


famous_name_(first = 'Md', last = 'Assaduzzaman', district = 'Nilphamari', stuyding = 'CS')


# return multiple things from function
def calcution(num1, num2):
    sum = num1 + num2
    mul = num1 * num2
    sub = num1 - num2
    return sum, mul, sub # return as a tuple
    return [sum, mul, sum] # return as a list

print(calcution(5, 3)) 

