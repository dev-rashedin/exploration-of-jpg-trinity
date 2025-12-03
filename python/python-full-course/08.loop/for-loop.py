# For loops = execute a block of code a fixed number of times. 
#             You can iterate over a range, string, sequence, etc 


# for x in (range(1, 11)):
#   print(x)


# for x in reversed(range(1, 11)):
#   print(x)


# for x in range(1, 11, 2):
#   print(x)

# the first parameter in range is the start value
# the second parameter is the end value
# the third parameter is the step value

credit_card = "1234-45445-43213-1341"

# for x in credit_card:
#   print(x)


# for x in range(1, 21):
#   if x == 13:
#       continue
#   else:
#       print(x)


for x in range(1, 21):
  if x == 13:
     break
  else:
      print(x)
