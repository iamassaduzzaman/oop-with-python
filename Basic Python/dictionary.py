# more like a map in dictionary
person = {'name' : 'chodu shahir', 'address' : 'yk-2', 'gf' : 'bilai', 'age' : '49'}

print(person)
del person['age']
for key, value in person.items():
    print(key, ': ', value)

