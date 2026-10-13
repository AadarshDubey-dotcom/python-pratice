#Exception handling
"""Exception Handling ka matlab hai ki program error aane par crash na ho,
 balki usko handle karke safely chalna continue kare."""

n = 10 
m = 0

try:
     ans = n/m
     print(ans)
except ZeroDivisionError:
     print("Error : Division by zero")

