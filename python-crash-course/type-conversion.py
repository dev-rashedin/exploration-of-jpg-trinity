# input function is used to take input from the user, and it returns a string
x = input('x: ') 

print(type(x)) # type is another built in python function that returns the type of the variable

y = int(x) + 1

print(f"x: {x}, y: {y}")

int(x) # convert string to integer
float(x) # convert string to float
bool(x) # convert string to boolean
str(x) # convert integer to string


# Falsy
# "" (empty string)
# 0
# None

# Truthy
# "Hello"
# 1 (any number other than 0)

bool(False)