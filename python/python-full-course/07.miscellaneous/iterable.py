# Iterables = An object/collection that can return its elements one at a time
#             allowing it to be iterated over in a loop


# lists are iterable
# Tuples are iterable
# Sets are iterable
# Strings are iterable
# Dictionaries are iterable


# numbers = [1, 2, 3, 4, 5]

# for num in reversed(numbers):
#     print (num, end="-")

# fruits = {'apple', 'banana', 'cherry', 'orange'}

# for fruit in sorted(fruits):
#   print(fruit, end=", ")

# name = 'Rashedin'

# for char in name:
#   print(char, end=" ")

my_dictionary = {
  'name': 'Rashedin',
  'age': 29,
  'gpa': 3.2
}

for key, value in my_dictionary.items():
  print(key, end=" ")
  print()
  print(value, end=" ")