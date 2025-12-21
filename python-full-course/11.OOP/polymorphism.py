# Polymorphism 
# Greek word that means to "have many forms or faces"

# Two ways to achieve polymorphism
# 1. Inheritance --> An object could be treated of the same type as a parent class
# 2. "Duck typing" --> An object could be treated of the same type as a parent class

from abc import ABC, abstractmethod

class Shape:
  
  @abstractmethod
  def area(self):
    pass


class Circle(Shape):
  
  def __init__(self, radius):
      self.radius = radius

  def area(self):
      return 3.14 * self.radius ** 2


class Rectangle(Shape):
  
  def __init__(self, width, height):
      self.width = width
      self.height = height

  def area(self):
      return self.width * self.height


class Square(Shape):
  
  def __init__(self, width):
      self.width = width

  def area(self):
      return self.width ** 2


class Triangle(Shape):
  
  def __init__(self, base, height):
      self.base = base
      self.height = height

  def area(self):
      return 0.5 * self.base * self.height


shapes = [Circle(4), Rectangle(5, 6), Square(5), Triangle(3, 4)]


for shape in shapes:
  print(f"The area of the {type(shape).__name__} is {shape.area()}cm²")

