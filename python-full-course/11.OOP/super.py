# super()
# - Function used in a child class to call methods from a parent class (super class)
# - Allows you to extend the functionality of the inherited methods


class Shape:
  def __init__(self, color, filled):
    self.color = color
    self.filled = filled

  def describe(self):
    print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
  def __init__(self, color, filled, radius):
    super().__init__(color, filled)
    self.radius = radius

  def describe(self):
    super().describe()
    print(f"It is a circle with an area of {3.14 * self.radius ** 2}cm²")

class Square:
  def __init__(self, color, filled, width):
    super().__init__(color, filled)
    self.width = width

  def describe(self):
    super().describe()
    print(f"It is a square with an area of {self.width ** 2}cm²")

class Triangle:
  def __init__(self, color, filled, base, height):
    super().__init__(color, filled)
    self.base = base
    self.height = height

  def describe(self):
    super().describe()
    print(f"It is a triangle with an area of {0.5 * self.base * self.height}cm²")



circle = Circle(color='red', filled= True, radius=5)

# print(f"Circle color: {circle.color}, filled: {circle.filled}, radius: {circle.radius}")


circle.describe()