#3.	w.a.p to use featori
# loop logic

num = int(input("Enter the Number:"))
fact = 1

for i in range(1, num + 1):
    fact *= i
     
    print("The factorial of", num, "is", fact)

# for factorial 

def factorial(n):
     if n == 0 or n == 1:
          return 1