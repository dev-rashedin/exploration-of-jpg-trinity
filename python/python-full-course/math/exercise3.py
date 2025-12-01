import math

a = int(input('Enter side A: '))
b = int(input('Enter side B: '))


c = pow(a, 2) + pow(b, 2)

c = math.sqrt(c)

print(f"The length of the hypotenuse is {round(c, 2)}")

