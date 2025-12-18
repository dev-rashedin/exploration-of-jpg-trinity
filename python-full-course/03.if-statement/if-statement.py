# if = Do some code only if some condition is True
#      Else do something else

age = int(input('Enter your age:'))

if age >= 100:
    print('You are too old to open an account')
elif age >= 18:
    print('Your are eligible to open an account')
elif age < 0:
    print("You haven't been born yet")

else:
    print('You are not eligible to open an account')
