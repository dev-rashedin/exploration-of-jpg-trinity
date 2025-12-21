# super()
# - Function used in a child class to call methods from a parent class (super class)
# - Allows you to extend the functionality of the inherited methods


class Shape:
  def __init__(self, color, filled):
    self.color = color
    self.filled = filled

class Circle(Shape):
  def __init__(self, color, filled, radius):
    super().__init__(color, filled)
    self.radius = radius

class Square:
  def __init__(self, color, filled, width):
    super().__init__(color, filled)
    self.width = width

class Triangle:
  def __init__(self, color, filled, base, height):
    super().__init__(color, filled)
    self.base = base
    self.height = height

