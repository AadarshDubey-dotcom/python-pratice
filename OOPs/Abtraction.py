from abc import ABC, abstractmethod

class Vehicle(ABC):
     @abstractmethod
     def start(self):
          pass
     
class Car(Vehicle):
     def start(self):
          return "Car engin start with a key"
          
class Bike(Vehicle):
     def start(self):
          return "Bike engin start with a key"
          
c = Car()          
b = Bike()

print(c.start())
print(b.start())

#Abstraction is a process of hiding the implementation details and showing only functionality to the user. In Python, abstraction can be achieved by using abstract classes and methods. An abstract class is a class that cannot be instantiated and is meant to be subclassed. It can contain abstract methods, which are methods that are declared but contain no implementation. Subclasses of the abstract class must provide implementations for the abstract methods.