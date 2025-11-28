course = ' python programming for beginners '

print(course.upper()) # prints the string in upper case

print(course.lower()) # prints the string in lower case

print (course.title()) # prints the string in title case

print(course.strip()) # prints the string without the white spaces

print(course.lstrip()) # prints the string without the left white spaces

print(course.rstrip()) # prints the string without the right white spaces

print(course.find('for')) # prints the index of the string

print(course.find('For')) # Python is case sensitive and it will print -1 as it can't find the string

print(course.replace('p', 'j')) # prints the string with the replaced character

print('python' in course) # prints True or False
 
print('swift' not in course) # prints True or False
print('python' not in course) # prints True or False