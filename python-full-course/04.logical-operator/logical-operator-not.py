## logical operators = evaluate multiple conditions (or, and, not)
##                or = at least one condition must be true
##                and = all conditions must be true
##                not = reverse the condition (not False, not True)

temp = 15
is_sunny = False

if temp >= 28 and is_sunny:
  print('It is hot outside')
elif temp <= 15 and not is_sunny:
  print('It is a cool day')
  print('It is cloudy')
elif temp <= 0 and not is_sunny:
  print('It is freezing outside')
  print('It is cloudy')
elif 28 > temp > 0 and is_sunny:
  print('It is warm outside')
  print('It is sunny')
