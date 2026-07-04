#Suare of number 
n = int(input("enter the number :"))
def square(n):
     return n**2
     
print(square(n))     

#check even or odd
n = int(input("Enter the Number :"))

def even_and_odd(n):
     if (n % 2 == 0):
          return "Even"
     else:
          return "Odd"
          
print(even_and_odd(n))          

#list of sum 

number = list(map(int, input("Enter numbers separated by space: ").split()))

def sum_of_list(number):
    total = 0
    for num in number:
        total = total + num
    return total

print("Sum of list =", sum_of_list(number))

#reverse of string method one slice method
string =  input("Enter text : ")

def reverse(string):
     return string[::-1]
     
print(reverse(string))

#method second using loop
string =  input("Enter text : ")

def reverse(string):
     rev = ""
     for ch in string:
          rev = ch + rev
     return rev  
     
print(reverse(string))