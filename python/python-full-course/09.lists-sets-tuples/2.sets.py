# collections = single "variable" used to store multiple values
# List = [] ordered and changeable, Duplicates OK
# Set  = {} unordered and immutable, but Add/Remove OK. NO Duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER



# sets in python, array in js, vector in golang  

# we cannot access items by index
# we cannot change items
# we can add items
# we can remove items

fruits = {'apple', 'banana', 'cherry', 'orange'}

# print(dir(fruits)) # To get all the methods

# print(help(fruits)) # To get all the methods

# print(len(fruits)) # To get the length of the set

# print('apple' in fruits) # To check if the item is in the set

# print('pineapple' in fruits) # To check if the item is in the set


fruits.add('mango') # To add item to the set

fruits.remove('apple') # To remove item from the set

fruits.pop() # To remove the last item from the set (It will be random)

fruits.clear() # To clear the set

print(fruits)