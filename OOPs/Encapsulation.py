# create  Bank Account using Python OOPs concept
class BankAccount:
     def __init__(self, owner, balance):
          self.owner = owner
          self.__balance = balance
          
     def get_balance(self):
          return self.__balance
          
     def deposit(self, amount):
          if amount > 0:
               self.__balance += amount
               
     def withdraw(self, amount):
          if 0 < amount <= self.__balance:
               self.__balance -= amount

acc = BankAccount("Harh", 1000)               
print(acc.get_balance())
acc.deposit(505)
print(acc.get_balance())
acc.withdraw(200)
print(acc.get_balance())

# create Student Encapsulation in python 
class Student:
     def __init__(self, name):
          self.name = name
          self.__marks = 0
          
     def get_marks(self):
          return self.__marks
          
     def set_marks(self, marks):
          if marks >= 0 and marks <= 100:
             self.__marks = marks
             
          else:
               print("invaild marks")
               
s1 = Student('harsh')               
s1.set_marks(67)
print(s1.get_marks())

#create Employee Inheritance  in python
class Empolyee:
     def __init__(self, name, salary):
          self.name = name
          self.salary = salary
          
     def show_detail(self):
          return f"Name: {self.name} salary: {self.salary}"
          
class Manager(Empolyee):
     def manage_team(self):
          return f"{self.name} is manage the team"
          
class Developer (Empolyee):
     def write_code(self):
          return f"{self.name} is writting code"
          
m1 = Manager("harsh", 59000)          
d1 = Developer("Adarsh", 67888)

print(m1.show_detail())
print(m1.manage_team())

print(d1.show_detail())
print(d1.write_code())
