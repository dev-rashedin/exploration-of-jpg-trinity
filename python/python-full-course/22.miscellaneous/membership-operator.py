# Membership operators = used to test whether a value or variable is found in a sequence (string, list, tuple, set or dictionary)
#                      1. in
#                      2. not in



# fruits = ['apple', 'banana', 'cherry', 'orange']

# if 'apple' in fruits:
#   print("apple is my favorite fruit")

# if 'pineapple' not in fruits:
#   print("pineapple is not my favorite fruit")


grades = {
  "Alex": 80,
  "John": 90,
  "Jane": 85,
  "Alice": 95,
  "Bob": 75,
  "Sarah": 100
}

student = input("Enter a student name: ").capitalize()

if student in grades:
  print(f"{student} has a grade of {grades[student]}")
else:
  print(f"{student} is not in the class")