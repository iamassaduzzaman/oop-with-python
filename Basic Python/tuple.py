def multiple():
    return 2, 3

print(multiple())

things = 'panir bottle', 'pranto', 'mobile', 'bhaiya', 'apu', 'food court'

print(type(things))
print(things[0])
print(things[-2])
print(things[2:3])

if 'mobile' in things:
    print('mobile')

for item in things:
    print(item)

# tuple is immutalbe
things[0] = 'me'

mega = ([2, 3, 4], [5, 6, 7])
print(mega)


