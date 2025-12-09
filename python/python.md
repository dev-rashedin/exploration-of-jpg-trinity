
# 🐍 Beginner-Friendly Guide to Python

*A complete guide for absolute beginners — simple English, clear examples.*

---

## 1. What is Python?

Python is a **high-level**, **beginner-friendly**, **general-purpose** programming language.  
It is used for web development, data science, machine learning, automation, backend development, cybersecurity, and DevOps.  

Python is famous because it is readable and simple. Example:

```python
print("Hello, world!")
```

---

## 2. A Short History of Python

**How Python Was Born**  
- Created by **Guido van Rossum** in **1989**.  
- First released in **1991**.  
- Guido wanted a language that was simple, readable, and powerful.  
- Named after the comedy group **“Monty Python”**, not the snake.

**Evolution**  
- **Python 2** (2000): Easy scripting but had design limitations.  
- **Python 3** (2008): Modernized, cleaned up issues from Python 2.  
- Python 3 is now the main version used worldwide.

**Why Python Became Popular**  
- Readable and easy to write.  
- Less code → more productivity.  
- Huge ecosystem: Django, Flask, NumPy, Pandas, TensorFlow, etc.  
- High demand in 2026: Backend developers, AI/ML engineers, and data scientists prefer Python.

---

## 3. How Python Runs

Python is commonly called an **interpreted language**, but its process is a mix of interpreting and compiling.

### How Python Executes Code (Step by Step)

When you run a Python file:

1. **You write `.py` code**  
2. Python **compiles it into bytecode** (`.pyc` files)  
3. The **Python Virtual Machine (PVM)** executes the bytecode  

This makes Python flexible and portable.

---

## Different Implementations of Python

### 1. CPython (The Default)

- Most popular version  
- Written in C  
- Converts Python code → bytecode → interprets it  
- What you get when you install Python from python.org

### 2. Jython

- Runs Python on the **Java Virtual Machine (JVM)**  
- Lets you use Java libraries in Python  
- Useful in Java-heavy companies

### 3. PyPy

- Faster implementation of Python  
- Uses a **Just-In-Time (JIT)** compiler  
- Good for performance-heavy tasks

---

## Why Python Uses This Design

Python focuses on:

- **simplicity**
- **developer productivity**
- **flexibility**

If Python compiled directly to machine code like C or Go:

- code would be harder to write  
- dynamic typing would be more limited  
- debugging would be less friendly  

Python chooses simplicity and flexibility over raw speed, which is why it remains one of the best beginner languages.

---

---

## 4. Python Basics

Python is simple, but powerful. This section explains its core building blocks in beginner‑friendly language with examples.

---

## 4.1 Variables and Data Types

A **variable** is a container that stores a value.  
Think of it like a labeled box where you keep information.

### Key Points
- Variables store data such as text, numbers, true/false values, lists, etc.
- Variables are **case‑sensitive** (`name` and `Name` are different).
- Python uses **dynamic typing**, meaning you don’t have to declare a type.

### Example
```python
name = "Alice"       # string
age = 25             # integer
height = 5.7         # float
is_student = True    # boolean
```

---

## Typecasting

**Typecasting** means converting one data type into another.

### Built‑in Functions
- `str()` → convert to string  
- `int()` → convert to integer  
- `float()` → convert to floating number  
- `bool()` → convert to boolean  

### Example
```python
age = "25"
age_number = int(age)   # "25" → 25 (integer)
print(type(age_number))
```

---

## input()

`input()` allows the user to enter data from the keyboard.

- Always returns data as a **string**.
- Convert it using typecasting if needed.

### Example
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # convert to integer
print("Hello,", name)
print("You are", age, "years old")
```

---

## 4.2 Operators

Operators perform actions on values.

### Arithmetic Operators
| Operator | Meaning      | Example |
|---------|--------------|---------|
| +       | Add          | 3 + 2   |
| -       | Subtract     | 5 - 1   |
| *       | Multiply     | 2 * 4   |
| /       | Divide       | 9 / 2   |
| %       | Modulus      | 10 % 3 → 1 |
| **      | Power        | 2 ** 3 → 8 |


### Built in math functions
x = 3.14
y = -4
z = 5

- result = round(x)

- result = abs(y)

- result = pow(4, 3)

- result = max(x, y, z)

result = min(x, y, z)

print(result)


### Math modules

import math

print(math.pi)
print(math.e)

result = math.sqrt(16)

result = math.ceil(2.1)

result = math.floor(2.9)

print(result)


# if Statement
 - Do some code only if some condition is True
 - Else do something else

age = int(input('Enter your age:'))

if age >= 100:
    print('You are too old to open an account')
elif age >= 18:
    print('Your are eligible to open an account')
elif age < 0:
    print("You haven't been born yet")

else:
    print('You are not eligible to open an account')


### Comparison Operators
Used to compare values (returns True or False):

`==`, `!=`, `<`, `>`, `<=`, `>=`

### Logical Operators
 - evaluate multiple conditions (or, and, not)
   - or = at least one condition must be true
   - and = all conditions must be true
   - not = reverse the condition (not False, not True)

```
temp = 15
is_sunny = False

if temp >= 28 or is_sunny:
  print('It is hot outside')
elif temp <= 15 and not is_sunny:
  print('It is a cool day')
  print('It is cloudy')
elif temp <= 0 and not is_sunny:
  print('It is freezing outside')
  print('It is cloudy')
elif 28 > temp > 0 and is_sunny:
  print('It is warm outside')
  print('It is sunny')
```

# conditional expression 
 - A one-line shortcut for the if-else statement (ternary operator)
 - Print or assign one of two values based on a condition
 - X if condition else Y

 ```
num = 5
a = 6
b = 7

print('Positive' if num > 0 else 'Negative')

print('Positive' if num > 0 else 'Negative')


result = 'Even' if num % 2 == 0 else "Odd"

max_num = a if a > b else b

print(f"The maximum number is {max_num}")

min_num = a if a < b else b

print(f"The minimum number is {min_num}")

 ```


## String method

```
name = "rashedin islam"

len(name) # Returns the length of the string

name.upper() # Returns the string in upper case

name.lower() # Returns the string in lower case

name.find('s') # Returns the index of the specified string. It will give the first index. if it is not found, it returns -1

name.rfind('a') # Returns the index of the specified string. It will give the last index. if it is not found, it returns -1

name.capitalize()  # Returns the string in title case (the first letter of the string will be in upper case )

name.title()  # Returns the string in title case (the first letter of each word will be in upper case )

name.isdigit()  # Returns True if the string contains only digits

name.isalpha()  # Returns True if the string contains only alphabetic characters

name.isnumeric()  # Returns True if the string contains only digits

name.count("a") # Returns the number of times a specified value occurs in a string

number.replace("", "-") # Replaces all occurrences of a specified value with another value
```


## Indexing in String

- Accessing element of a sequence using [] (indexing operator)
- [start: end : stop]

```
credit_number = "1234-45445-43213-1341"

credit_number[0] # gives the first character in the string

credit_number[0: 4] # gives the first 4 characters in the string
credit_number[: 4] # gives the first 4 characters in the string
credit_number[4: 8] # gives the next 4 characters in the credit_number[5:] # gives all characters after the 5th character in the string
credit_number[-3] # gives the number form the end
credit_number[0 : 4 : 2] # gives the first 4 characters in the string with a step of 2
credit_number[::2] # gives all characters in the string with a step of 2
```
---

## Example Program Using Everything
```python
name = input("Your name: ")

age = int(input("Your age: "))

if age >= 18 and age <= 60:
    print("Hello", name, "- You are an adult.")
elif age > 60:
    print("Hello", name, "- You are a senior.")
else:
    print("Hello", name, "- You are a minor.")

print("Age squared:", age ** 2)
print("Is your age even?", age % 2 == 0)
```



### 4.3 Loops
```python

# while loop 
# execute some code WHILE some condition remain true

name = input('Enter your name: ')

while  name == '':
  print('You did not enter your name')
  name = input('Enter your name: ')
else:
  print(f'Hello {name}')

# For loops 
# execute a block of code a fixed number of times. 
# You can iterate over a range, string, sequence, etc 


for x in (range(1, 11)):
  print(x)


for x in reversed(range(1, 11)):
  print(x)


for x in range(1, 11, 2):
  print(x)

# the first parameter in range is the start value
# the second parameter is the end value
# the third parameter is the step value

# For loop is count based (when we know how many time it's going to run)

# While loop is condition based (when we don't know how many time it's going to run)

# nested loop 
# a loop within another loop (outer, inner)
# outer loop:
#   inner loop:


for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print()

```

## collections = single "variable" used to store multiple values
### List = [] ordered and changeable, Duplicates OK
### Set  = {} unordered and immutable, but Add/Remove OK. NO Duplicates
### Tuple = () ordered and unchangeable. Duplicates OK. FASTER

### List

```python
# list in python, array in js, vector in golang
fruits = ['apple', 'banana', 'cherry', 'orange']

print(fruits[0]) # comment to describe it

print(fruits[::-1]) # comment to describe it

for fruit in fruits: # comment to describe it
# print(fruit)

dir(fruits) # To get all the methods

help(fruits) # comment to describe it

len(fruits) # comment to describe it

print('apple' in fruits) # comment to describe it 
print('pineapple' in fruits) # comment to describe it

fruits[1] = 'pineapple' # change item

fruits.append('mango')  # add item to the end of the list

fruits.remove('apple') # remove item

fruits.insert(1, 'kiwi') # insert item at preferred index

fruits.insert(0, 'apple')

fruits.sort() # sort the list in the alphabetical order

fruits.reverse()  # reverse the list

# fruits.clear() # clear the list

appleIndex = fruits.index('apple') # returns the index of the item

print(appleIndex)

bananaCount = fruits.count('banana') # returns the number of times the item appears in the list

print(bananaCount)
```

# Set
```python
# sets in python, array in js, vector in golang  

# we cannot access items by index
# we cannot change items
# we can add items
# we can remove items

fruits = {'apple', 'banana', 'cherry', 'orange'}

print(dir(fruits)) # To get all the methods

print(help(fruits)) # To get all the methods

print(len(fruits)) # To get the length of the set

print('apple' in fruits) # To check if the item is in the set

print('pineapple' in fruits) # To check if the item is in the set

fruits.add('mango') # To add item to the set

fruits.remove('apple') # To remove item from the set

fruits.pop() # To remove the last item from the set (It will be random)

fruits.clear() # To clear the set
```

```python
# tuple in python, array in js, vector in golang
# tuple are ordered and unchangeable. Duplicates OK, Faster than lists
fruits = ('apple', 'banana', 'cherry', 'orange')

print(dir(fruits)) # To get all the methods

print(help(fruits)) # To get all the methods

print(len(fruits)) # To get the length of the tuple

print('apple' in fruits) # To check if the item is in the tuple

print('pineapple' in fruits) # To check if the item is in the tuple

fruits.index('apple') # To get the index of the item

fruits.count('apple') # To get the number of times the item is in the tuple

for fruit in fruits:
  print(fruit)
```

### 4.5 Functions
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

### 4.6 Lists and Dictionaries
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple

person = {"name": "Alice", "age": 25}
print(person["name"])  # Alice
```

---

## 5. Conclusion

Python is **beginner-friendly**, **versatile**, and has a **huge ecosystem**.  
Its readable syntax, flexibility, and demand make it an excellent first programming language.  

Whether you want to do **web development**, **AI**, or **automation**, Python is the go-to choice for beginners in 2026 and beyond.
