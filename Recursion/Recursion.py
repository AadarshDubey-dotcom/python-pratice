#Recursion
"""Simple Example: Factorial (n!)Maano hume 5! = 5 * 4 * 3 * 2 * 1 = 120 nikaalna hai.Formula: n! = n * (n - 1)! Base case: 0! = 1 ya 1! = 1"""
def factorial(n: int) -> int:
     if n <= 1:
          return 1
     return n * factorial(n-1)
     
print(factorial(5)) 

""" Reverse a String (Basic Recursion)
- Problem: Ek character list ya string s di gayi hai. Bina built-in reverse ya extra array banaye, recursion ka use karke ise reverse karo.
- Example: ["h", "e", "l", "l", "o"] rightarrow ["o", "l", "l", "e", "h"]
- Hint: Do pointers (left, right) ko recursive function mein pass karo; swap karke left + 1, right - 1 call karo jab tak left < right ho."""
def reverse_string(s: list[str], left: int = 0, right: int | None = None) -> None:
     if right is None:
          right = len(s) - 1
