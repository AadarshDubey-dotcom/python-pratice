#Recursion
"""Simple Example: Factorial (n!)Maano hume 5! = 5 * 4 * 3 * 2 * 1 = 120 nikaalna hai.Formula: n! = n * (n - 1)! Base case: 0! = 1 ya 1! = 1"""
def factorial(n: int) -> int:
     if n <= 1:
          return 1
     return n * factorial(n-1)
     
print(factorial(5)) 