# validate user input exercise

# 1. username is no more than 12 characters
# 2. username is no less than 3 characters
# 3. username must not contain any spaces
# 4. username must contain digits


username = input('Enter your username: ')

error_message = "username cannot be less than 3 characters or more than 12 characters or contain spaces or digits"


# print(f"hello {username}" if 3 <= len(username) <=
#       12 and username.isdigit() else error_message)

if 3 <= len(username) <= 12 and username.isalpha() :
  print(f"hello {username}")
else:
  print(error_message)
