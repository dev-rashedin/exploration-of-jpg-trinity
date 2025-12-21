# multiple inheritance -->
# - multiple inheritance inherit from more than one paren class C(A, B)
# multi-level inheritance -->
# - multi-level inheritance inherit from a parent class that inherits from another parent class


class Animal:

  def __init__(self, name):
    self.name = name
    
  def eat(self):
    print(f"The {self.name} is eating")

  def sleep(self):
    print(f"The {self.name} is sleeping")

class Prey(Animal):
  def flee(self):
    print(f"The {self.name} is fleeing")

class Predator(Animal):
  def hunt(self):
    print(f"The {self.name} is hunting")

class Rabbit(Prey):
  pass

class Hawk(Predator):
  pass

class Fish(Prey, Predator):
  pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()

hawk.hunt()

fish.flee()
fish.hunt()