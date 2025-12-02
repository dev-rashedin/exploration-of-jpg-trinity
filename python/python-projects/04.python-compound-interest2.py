# Python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
  principle = float(input('Enter the principle amount: '))
  if principle < 0:
    print('Principle amount must be greater than 0')
  else:
    break


while True:
  rate = float(input("Enter the rate of interest: "))
  if rate < 0:
    print('Rate of interest must be greater than 0')
  else:
    break


while True:
  time = int(input('Enter the number of years: '))
  if time < 0:
    print('Number of years must be greater than 0')
  else:
    break
 

total = principle * pow((1 + rate / 100), time)

print(f'The total balance after {time} year/s is: ${round(total, 2)}')
