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

class Parent:
     def show(self):
          print("this is parent class")
          
class child(Parent):
     def display(self):
          print("this is child class")
          
obj = child()          
obj.show()
obj.display()

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

class Person:
     def __init__(self, name):
          self.name = name
          
     def show_name(self):
          print(f"Name: {self.name}")
     
class Student(Person):
     def __init__(self, name, roll_no):
          super().__init__(name)
          self.roll_no = roll_no
          
     def show_roll(self):
          print(f"roll_no : {self.roll_no}")
          
class Exam(Student):
     def __init__(self, name, roll_no, marks):
          super().__init__(name, roll_no)
          self.marks = marks
          
     def show_marks(self):
          print(f"{self.name} (Roll {self.roll_no}) scored {self.marks}")
          
obj = Exam('Adarsh', 101, 78)          
obj.show_name()
obj.show_roll()
obj.show_marks()
          
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

class BankAcount:
     def __init__(self, account_number, balance=0):
          self.account_number = account_number
          self.balance = balance
          
     def deposit(self, amount):
          self.balance += amount
          print(f"Deposit {amount}, New Balance: {self.balance}")
     
     def withdraw(self, amount):
          if self.balance >= amount:
               self.balance -= amount
               print(f"withdraw {amount}, Reaming amount: {self.balance}")
          else:
               print("Insufficient fund")

class SavingAccount(BankAcount):
     def __init__(self, account_number, balance=0, interest_rate=5):
          super().__init__(account_number, balance)
          self.interest_rate = interest_rate
          
     def add_interest(self):
          interest = self.balance * self.interest_rate /100
          self.balance += interest
          print(f"interest added: {interest}, New Balance: {self.balance}")

class CurrentAccount(BankAcount):
     def __init__(self, account_number, balance=0, overdraf_limit=1000):
          super().__init__(account_number, balance)
          self.overdraf_limit = overdraf_limit
          
     def withdraw(self, amount):
          if self.balance + self.overdraf_limit >= amount:
               self.balance -= amount
               print(f"withdraw {amount}, Reaming balance: {self.balance}")
          else:
               print("overdraft limit exceeded")

class LoanAccount(BankAcount):
     def __init__(self, account_number, balance=0, loan_amount=0):
          super().__init__(account_number, balance)
          self.loan_amount = loan_amount
          
     def pay_emi(self, emi):
          self.loan_amount -= emi
          print(f"emi paid: {emi}, Reaming loan: {self.loan_amount}")

saving = SavingAccount("khkjhdskj", 1000)
saving.deposit(500)
saving.add_interest()

current = CurrentAccount("ggjgjg", 200)
current.withdraw(1000)

loan = LoanAccount("IUS", 0, 50000)
loan.pay_emi(5000)

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
