# Inheritance
# Inheritance allows a class to inherit attributes and methods from another class
# It helps with code reusability and extensibility
# class Child(parent)


class Animal:

  def __init__(self, name):
    self.name = name
    self.is_alive = True

  def eat(self):
    print(f"{self.name} is eating")

  def sleep(self):
    print(f"{self.name} is sleeping")


class Dog(Animal):
   
  def speak(self):
    print(f"{self.name} is barking")

class Cat(Animal):

  def speak(self):
    print(f"{self.name} is meowing")

class Mouse(Animal):
   
  def speak(self):
    print(f"{self.name} is squeaking")


dog = Dog("Scooby")
cat = Cat("Meow")
mouse = Mouse("Mickey")


dog.speak()
cat.speak()
mouse.speak()