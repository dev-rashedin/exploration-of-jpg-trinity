# Variable scope
# - Where a variable is visible and accessible
# scope resolution --> (LEGB) --> Local -> Enclosed -> Global -> Built-in


# example of local scope
def func1():
    x = 1
    print(x)


def func2():
    x = 2
    print(x)

# example of enclosed scope


def func1():
    x = 1
    print(x)

    def func2():
        print(x)


# example of global scope
x = 3

def func1():

    print(x)


def func2():
    print(x)


func1()
func2()

# example of built-in scope

from math import e

def func1():
    print(e)


