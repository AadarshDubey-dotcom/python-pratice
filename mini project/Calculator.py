# make calulator in python

#define function 
def add(a, b):
     return a + b

def Subtraction(a, b):
     return a - b
     
def Multiplication(a, b):
     return a * b 

def Division(a, b):
     if b != 0:
          return a / b
     else:
          return "Error! Division by Zero"
          
#Take user input
print("Select operation: 1.Add 2.Subtraction 3.Multiplication 4.Division")
choice = input("Enter choice (1/2/3/4):")

num1 = int(input("Enter First number :"))
num2 = int(input("Enter Second number :"))

#call function based on choice
if choice == "1":
     print("Result :", add(num1, num2))
elif choice == "2":
     print("Result :", Subtraction(num1, num2))
elif choice == "3":
     print("Result :", Multiplication(num1, num2))
elif choice == "4":
     print("Result :", Division(num1, num2))
else:
     print("invalid choice")