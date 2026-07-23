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