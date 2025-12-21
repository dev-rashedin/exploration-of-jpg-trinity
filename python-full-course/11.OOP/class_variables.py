# class variables 
# - class variables is shared among all instances of a class
# - defined outside the constructor
# - allow you to share data among all objects created from that class

class Student:

  class_year = 2025
  num_students = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age
    Student.num_students += 1


student1 = Student("Rashedin", 29)
student2 = Student("Arjuman", 30)
student3 = Student("Sophie", 29)


# print(student1.name)
# print(student2.name)


print(Student.class_year)
print(Student.num_students)