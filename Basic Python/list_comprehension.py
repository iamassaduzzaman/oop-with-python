numbers = [45, 87, 96, 65, 43, 90, 85, 14, 26, 61, 70]

odds = []

for num in numbers:
    if num % 2 == 1:
        odds.append(num)

print(odds)

# or
evens = [num for num in numbers if num % 2 == 0]
print(evens)