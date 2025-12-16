# List Comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]


# doubles = []

# for x in range(1, 11):
#   doubles.append(x * 2)

# print(doubles)


# doubles = [x*2 for x in range(1, 11)]

# print(doubles)

# triples = [x*3 for x in range (1,7)]

# print(triples)

# square = [x*x for x in range(1,5)]

# print(square)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newList = [fruit.capitalize() for fruit in fruits]

# print(newList)

numbers = [1, -4, 8, -9, -2, 6, 3, -1, 5, -7, 6, 8, 12, 3, 5, 7]

# positive_num = [num for num in numbers if num > 0]

# print(positive_num)

# even_num = [ num for num in numbers if num > 0 and num % 2 == 0]
# odd_num = [ num for num in numbers if num > 0 and num % 2 == 1]

even_num = [num for num in numbers if num % 2 == 0]
odd_num = [num for num in numbers if num % 2 ==1]

print(even_num)
print(odd_num)
