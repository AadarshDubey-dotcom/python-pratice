# Single inheritance in python
class Animal:
     def speak(self):
          return "Some sound"
          
class Dog(Animal):
     def speak(self):
          return "brak"

s2 = Animal()
print(s2.speak())

s1 = Dog()
print(s1.speak())

#Multilevel Inheritance in python
class Grandfather:
     def property(self):
          return "Land"
          
class Father(Grandfather):
     def House(self):
          return "House"
          
class Son(Father):
     def Car(self):
          return "car"
          
s = Son()          
print(s.property())
print(s.House())
print(s.Car())

#multiple inheritance in python
class Mom:
     def skill(self):
          return "Cooking"
          
class Dad:
     def skill(self):
          return "Driving"
          
class Son(Mom, Dad):
          pass
     
s = Son()
print(s.skill())

#Hierarchical Inheritance in python
class Animal:
     def speak(self):
          return "some sound"
          
class Dog(Animal):
     def speak(self):
          return "brak"
          
class Cat(Animal):
     def speak(self):
          return "meow"
          
c = Cat()          
print(c.speak())

d = Dog()
print(d.speak())

#Hybrid Inheritance in python
class A:
     def methodA(self):
          return "method from A"
          
class B(A):             #single inheritance
     def methodB(self):
          return "method from B"
          
class C(A):            #Hierarchical Inheritance
     def methodC(self):
          return "method from C"
          
class D(B, C):         #nutliple inheritance 
     def methodD(self):
          return "method from D"
          
s = D()          
print(s.methodA())
print(s.methodB())
print(s.methodC())
print(s.methodD())
