# in, not, not in, is, is not 
# >, <, >=, <=, ==, !==
# and, or

number = 3
is_sleeping = True

# condition
if number > 9:
    print('Number is greater than 9')
else:
    print('Number is less than 9')


# nested conditions
if number > 9:
    if is_sleeping is True:
        print('Assaduzzaman is sleeping')
    else:
        print('Assaduzzaman is not sleeping')
else:
    print('Assaduzzaman is not sleeping')

# multiple condition
if number > 10:
    print('Number is greater than 10')
elif number > 5:
    print('Number is greater than 5 and less than 10')
else:
    print('Number is less than 5')

