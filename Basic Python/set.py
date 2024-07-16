# list --> []
# tuple --> ()
# set --> {}
# set: unique items collection. No duplicate

numbers = [1, 2, 3, 4, 4, 5, 5, 6, 6, 6]

print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(7)
numbers_set.add(7)
numbers_set.add(7)
print(numbers_set)
numbers_set.remove(6)
print(numbers_set)

for item in numbers_set:
    print(item)