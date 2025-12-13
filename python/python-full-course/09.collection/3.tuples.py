# collections = single "variable" used to store multiple values
# List = [] ordered and changeable, Duplicates OK
# Set  = {} unordered and immutable, but Add/Remove OK. NO Duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# tuple in python, array in js, vector in golang
fruits = ('apple', 'banana', 'cherry', 'orange')

print(dir(fruits)) # To get all the methods

print(help(fruits)) # To get all the methods

print(len(fruits)) # To get the length of the tuple

print('apple' in fruits) # To check if the item is in the tuple

print('pineapple' in fruits) # To check if the item is in the tuple

appleIndex = fruits.index('apple') # To get the index of the item

fruits.count('apple') # To get the number of times the item is in the tuple

for fruit in fruits:
  print(fruit)

print(appleIndex)


print(fruits)