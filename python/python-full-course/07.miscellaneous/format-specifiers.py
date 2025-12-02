# format specifiers = {:flags} format a value based on what flags are inserted
# :.(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator


## Practice

price1 = 3.14159
# price2 = -987.65
price2 = -9870.65
price3 = 1200.34

# fixed decimal point
# print(f"price 1 is ${price1:.3f}")
# print(f"price 2 is ${price2:.3f}")
# print(f"price 3 is ${price3:.3f}")

# allocate spaces
# print(f"price 1 is ${price1:10}")
# print(f"price 2 is ${price2:10}")
# print(f"price 3 is ${price3:10}")

# zero pad
# print(f"price 1 is ${price1:010}")
# print(f"price 2 is ${price2:010}")
# print(f"price 3 is ${price3:010}")

# left justify
# print(f"price 1 is ${price1:<10}")
# print(f"price 2 is ${price2:<10}")
# print(f"price 3 is ${price3:<10}")

# right justify
# print(f"price 1 is ${price1:>10}")
# print(f"price 2 is ${price2:>10}")
# print(f"price 3 is ${price3:>10}")

# center
# print(f"price 1 is ${price1:^10}")
# print(f"price 2 is ${price2:^10}")
# print(f"price 3 is ${price3:^10}")

# insert a space before positive numbers
# print(f"price 1 is ${price1: }")
# print(f"price 2 is ${price2: }")
# print(f"price 3 is ${price3: }")

# comma separator
# print(f"price 1 is ${price1:,}")
# print(f"price 2 is ${price2:,}")
# print(f"price 3 is ${price3:,}")

# fixed decimal point and comma separator
print(f"price 1 is ${price1:+,.2f}")
print(f"price 2 is ${price2:+,.2f}")
print(f"price 3 is ${price3:+,.2f}")
