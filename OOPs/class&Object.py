#creating class in opython 
class Student:
    name = "Adarsh Dubey"

#Creating object in python 
s1 = Student()    
print(s1.name)

# __init__ Function (Contructor) 

#Creating class in python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#creating object in python
s1 = Student("Adarsh Dubey", 20)
print(s1.name)
print(s1.age)


# Method 
class Student:
     def __init__(self, fullname):
          self.fullname = fullname
          
     def hello(self):
          print("helllo", self.fullname)
          
s1 = Student("Adarsh")
s1.hello()

"""Class & Object Basics  
Ek Car class banao jisme attributes ho: brand, model, year.
Ek method car_info() likho jo car ka detail return kare. Fir 2 car objects banao aur unka info print karo."""
class Car:
     def __init__(self, brand, model, color):
          self.brand = brand
          self.model = model
          self.color = color
          
     def car_info(self):
               return f"{self.brand} {self.model} {self.color}"
               
c1 = Car("TATA", "suv", "black")
c2 = Car("Bmw", "M5", "white")

print(c1.car_info())
print(c2.car_info())

"""Mobile Class  
Ek Mobile class banao jisme attributes ho: brand, model, price. 
Ek method mobile_info() likho jo mobile ka detail return kare. Fir 2 mobile objects banao aur unka info print karo."""

class Mobile:
     def __init__(self, brand, model, price):
          self.brand = brand
          self.model = model
          self.price = price
          
     def mobile_info(self):
          return f"{self.brand} {self.model} {self.price}"
          
mobile1 = Mobile("OPPO", "A17k", 12000)
mobile2 = Mobile("Apple", "16 MAX", 56000)

print(mobile1.mobile_info())
print(mobile2.mobile_info())