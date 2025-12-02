# Exercise 2
# Shopping Cart Program

item = input('What do you want to buy? ')
price = float(input('What is the price? '))
quantity = int(input('How many do you want to buy? '))

total = int(price * quantity)

print(f'The total price of {quantity} {item} is BDT {total}')
