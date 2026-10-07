class Animal:
     def sound(self):
          return "Some generic sound."
          
class Dog(Animal):
     def sound(self):
          return "Bark"

class Cat(Animal):
     def sound(self):
          return "Meow"
          
animal = [Dog(), Cat(), Animal()]
for a in animal:
     print(a.sound())

# Polymorphism     
class Shape:
     def area(self):
          print("Area cannot be defined for generic shape")
class Circle(Shape):
     def __init__(self, radius):
          self.radius = radius
     
     def Area(self):
          return 3.14 * self.radius * self.radius
class Reactangle(Shape):
     def __init__(self, length, width):
          self.length = length
          self.width = width
          
     def Area(self):
          return self.length * self.width
          