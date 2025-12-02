# while loop = execute some code WHILE some condition remain true


# name = input('Enter your name: ')

# while  name == '':
#   print('You did not enter your name')
#   name = input('Enter your name: ')
# else:
#   print(f'Hello {name}')

# age = int(input('Enter your age: '))

# while age < 0:
#   print("Age cannot be negative")
#   age = int(input('Enter your age: '))

# print(f'You are {age} years old')


# food = input("Enter a food you like (q to quit): ")

# while not food == 'q':
#   print(f"I like {food}")
#   food = input("Enter another food you like (q to quit): ")

# print("No more food")

num = int(input('Enter a # between 1-10: '))

while num < 1 or num > 10:
  print(f"{num} is not valid")
  num = int(input('Enter a # between 1-10: '))

print(f"You entered {num}")

while not 1 > num > 10:
  print(f"{num} is not valid")
  num = int(input('Enter a # between 1-10: '))

print(f"You entered {num}")
