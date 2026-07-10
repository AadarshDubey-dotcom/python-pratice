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