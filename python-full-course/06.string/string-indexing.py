# indexing = accessing element of a sequence using [] (indexing operator)
#         = [start: end : stop]


credit_number = "1234-45445-43213-1341"

print(credit_number[0]) # gives the first character in the string
print(credit_number[0: 4]) # gives the first 4 characters in the string
print(credit_number[: 4]) # gives the first 4 characters in the string
print(credit_number[4: 8]) # gives the next 4 characters in the string
print(credit_number[5:]) # gives all characters after the 5th character in the string
print(credit_number[-3]) # gives the number form the end
print(credit_number[0 : 4 : 2]) # gives the first 4 characters in the string with a step of 2
print(credit_number[::2]) # gives all characters in the string with a step of 2