# for number in range(1, 10):
#   if number % 2 == 1:
#     continue
#   print(number)
# else:
#   print('we have 4 even numbers')


# for number in range(1, 10):
#    if number % 2 == 0:
#       print(number)
# print('we have 4 even numbers')

count = 0

for number in range(1, 10):
  if number % 2 == 0:
      count += 1
      print(number)

print(f'We have {count} even numbers')