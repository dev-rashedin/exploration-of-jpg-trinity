# Module
# - Module is a file containing code you want to include in your program
# - We need to use 'import' to include a module (built-in or our own code)
# - It's useful to break up a large program reusable separate files

import math
import math as m
from math import pi

import module_example

result = module_example.square(3)


print(result)