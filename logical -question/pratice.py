"""Exercise 1. Arithmetic Product and Conditional Logic
Practice Problem: Write a Python function that accepts two integer numbers.
If the product of the two numbers is less than or equal to 1000,
return their product; otherwise, return their sum."""

def check_number(a,b):
     product = a * b
     if product <= 1000:
          return Product
     else:
          return a+b
          
print(check_number(544,3))
print(check_number(44,65))

#Question: Write a program to check whether a given string is a palindrome or not.

word = input("enter the str :")

rev = "".join(reversed(word))

if word == rev:
     print("this is parlidrome.")
else:
     print("this is not parlidrome.")

#Two-Pointer Approach     

word = input("enter the word :")

left = 0
right = len(word) - 1
is_palidrome = True

while left < right:
     if word[left] != word[right]:
          is_palidrome = False
          break
     left += 1
     right -= 1
     
if is_palidrome:
     print("this is palidrome.")
else:
     print("this is not palidrome.")

#Armstrong number Ek number input lo aur check karo ki wo Armstrong number hai ya nahi (sum of cubes of digits = number).     

num = int(input("Enter the num :"))
cube_of_sum = 0
temp = num

while temp > 0:
     digit = temp % 10
     cube_of_sum += digit ** 3
     temp //= 10
     
if num == cube_of_sum:
     print("this is armstrong number.")
else:
     print("this is not amrstrong number.")     

"""Pattern printing  
Example:

Code
*
* *
* * *
* * * * iska logic"""

