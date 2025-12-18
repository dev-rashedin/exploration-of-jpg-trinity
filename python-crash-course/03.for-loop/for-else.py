successful = True


for number in range(3):
    print('Attempt')
    if successful:
        print('successful')
        break
else:
    print('Attempted 3 times and failed')