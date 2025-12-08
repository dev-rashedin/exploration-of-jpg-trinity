# collections = single "variable" used to store multiple values
# List = [] ordered and changeable, Duplicates OK
# sET  = {} unordered and immutable, but Add/Remove OK. NO Duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# list in python, array in js, vector in golang
fruits = ['apple', 'banana', 'cherry', 'orange']

# print(fruits[0])

# print(fruits[::-1])

# for fruit in fruits:
#   print(fruit)

# print(dir(fruits))

# print(help(fruits))

# print(len(fruits))

# print('apple' in fruits)
# print('pineapple' in fruits)

# fruits[1] = 'pineapple' # change item
# print(fruits)

fruits.append('mango')  # add item to the end of the list

fruits.remove('apple') # remove item

fruits.insert(1, 'kiwi') # insert item at preferred index

fruits.insert(0, 'apple')

fruits.sort() # sort the list in the alphabetical order

fruits.reverse()  # reverse the list

# fruits.clear() # clear the list

appleIndex = fruits.index('apple') # returns the index of the item

print(appleIndex)

bananaCount = fruits.count('banana') # returns the number of times the item appears in the list

print(bananaCount)

print(fruits)
