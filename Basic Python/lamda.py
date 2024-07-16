doubled = lambda num : num * 2

# print(doubled(2))

numbers = [1, 2, 3, 4, 5]

doubled_nums = map(lambda x: x * 2, numbers)
# print(list(doubled_nums))

students = [
    {'name' : 'shahir', 'age' : 24},
    {'name' : 'maruf', 'age' : 23},
    {'name' : 'nabil', 'age' : 28},
]

juniors = filter(lambda student : student['age'] < 25, students)
print(list(juniors))
