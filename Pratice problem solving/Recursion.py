 #  Factoria 
n = int(input("enter the number:"))

def fact(n):
     if n ==0:
          return 1
     return n * fact(n-1)     

print(fact(n))     

#print_number
n = int(input("enter the number:"))

def print_number(n):
     if n == 1:
          print(1, end=" ")
          return
     print_number(n-1)
     print(n, end=" ")
     
print_number(n)     
