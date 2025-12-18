## logical operators = evaluate multiple conditions (or, and, not)
##                or = at least one condition must be true
##                and = all conditions must be true
#                 not = reverse the condition (not False, not True)

temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
  print('It is hot outside')
elif temp <= 0 and is_sunny:
  print('It is freezing outside')
  print('It is sunny')
elif 28 > temp > 0 and is_sunny:
  print('It is warm outside')
  print('It is sunny')
