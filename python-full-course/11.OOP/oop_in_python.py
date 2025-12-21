# Object is A "bundle" of related attributes (variables) and methods (functions) 
# - Ex. phone, cup, book
# - You need a "class" to create many objects

# Class = (blueprint) used to design the structure and layout of an object

from car import Car


car1 = Car("Toyota", 2022, "red", True)
car2 = Car("Honda", 2021, "blue", False)

print(car1.model)
print(car2.year) 

print(car1.describe()) 
print(car2.describe())