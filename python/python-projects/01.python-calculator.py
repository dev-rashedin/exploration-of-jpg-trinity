## Python Calculator

operator = input('Enter the operator (+ - * /): ')

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

if operator == "+":
  result = num1 + num2
elif operator == "-":
  result = num1 - num2
elif operator == "*":
  result = num1 * num2
elif operator == '/':
  result = num1 / num2
else:
  print("Invalid operator")

 


print(f'The result is {round(result)}')