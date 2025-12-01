name = input('Enter your full name: ')

# Built in string methods
 
result = len(name) # Returns the length of the string

print(result)

result = name.upper() # Returns the string in upper case
print(result)

result = name.lower() # Returns the string in lower case



print(result)

result = name.find('s') # Returns the index of the specified string. It will give the first index. if it is not found, it returns -1


# Returns the index of the specified string. It will give the last index. if it is not found, it returns -1
result = name.rfind('a')

print(result)

result = name.capitalize()  # Returns the string in title case (the first letter of the string will be in upper case )

result = name.title()  # Returns the string in title case (the first letter of each word will be in upper case )

result = name.isdigit()  # Returns True if the string contains only digits

result = name.isalpha()  # Returns True if the string contains only alphabetic characters

print(result)

phone_number = input('Enter your phone number: ')

result = phone_number.isnumeric()  # Returns True if the string contains only digits

print(result)

