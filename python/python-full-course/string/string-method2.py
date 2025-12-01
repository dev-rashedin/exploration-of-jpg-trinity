phone_number = input('Enter your phone number: ')

result = phone_number.isnumeric()  # Returns True if the string contains only digits

result = phone_number.count("-") # Returns the number of times a specified value occurs in a string

result = phone_number.replace("-", " ") # Replaces all occurrences of a specified value with another value

print(result)


print(help(str))
