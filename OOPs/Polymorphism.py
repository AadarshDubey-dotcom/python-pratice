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
shape = [Circle(5), Reactangle(4,6)]

for s in shape:
     print(s.Area()) 

class calculator:
     def multiply(self, a=1, b=1, *args):
          result = a * b 
          for num in args:
               result *= num
          return result
     
calc = calculator()
print(calc.multiply())
print(calc.multiply(4))
print(calc.multiply(2,4))
print(calc.multiply(2,4,6))             