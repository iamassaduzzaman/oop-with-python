numbers = [12, 45, 98, 68]

numbers.append(60) # append the number back in the list

numbers.insert(0, 23) # insert the number in 0th position

if 98 in numbers:
    numbers.remove(98) # remove the element 98


last = numbers.pop() # take out the last element from the list/array
# print(last)

if 45 in numbers:
    idx = numbers.index(45) # return the index of a element
    # print(idx)


numbers.sort() # sort the list/array

numbers.reverse() # reverse the list/array

print(numbers)