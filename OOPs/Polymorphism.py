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