name = 'sakib\'s name' # escape

# multiple string
name2 = '''
yo, wassup?
how you doin' 
'''

# string is a sequence
for char in name2:
    print(char)

# this line will not work becase string is immutable
# name[0] = 'r'

print(name2[1:6])
print(name2[::-1])

if 'you' in name2:
    print('exist')

print(name.upper())



