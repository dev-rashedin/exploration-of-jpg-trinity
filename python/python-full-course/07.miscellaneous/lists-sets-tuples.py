# collections = single "variable" used to store multiple values
# List = [] ordered and changeable, Duplicates OK
# sET  = {} unordered and immutable, but Add/Remove OK. NO Duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER


fruits = ['apple', 'banana', 'cherry', 'orange']  # list in python, array in js, vector in golang

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

fruits.append('mango') # add item to the end of the list
print(fruits)