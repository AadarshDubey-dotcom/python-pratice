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