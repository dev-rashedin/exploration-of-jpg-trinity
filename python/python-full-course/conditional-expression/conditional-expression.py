# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y



num = 5
a = 6
b = 7

print('Positive' if num > 0 else 'Negative')

print('Positive' if num > 0 else 'Negative')


result = 'Even' if num % 2 == 0 else "Odd"

max_num = a if a > b else b

print(f"The maximum number is {max_num}")

min_num = a if a < b else b

print(f"The minimum number is {min_num}")

user_role = 'admin'

access_level = 'Admin-dashboard' if user_role == 'admin' else 'User-dashboard'

print(access_level)
