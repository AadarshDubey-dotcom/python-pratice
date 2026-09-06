# Reverse a number 
n = 1234
rev = 0

while n > 0:
     digit = n % 10
     rev = rev * 10 + digit
     n = n // 10
     
print("reverse num", rev)     

"""Reverse Number Logic Flow
Initialize reverse

rev = 0 rakha jata hai jo reversed number store karega.

Extract last digit

digit = num % 10 → ye number ka last digit nikalta hai.

Example: agar num = 1234 → digit = 4.

Add digit to reverse

rev = rev * 10 + digit → pehle se jo reversed number hai usko 10 se multiply karke naya digit add kar dete hain.

Isse digit ulte order me place hota hai.

Example: rev = 0*10 + 4 = 4.

Remove last digit

num = num // 10 → original number ka last digit hata dete hain.

Example: 1234 // 10 = 123.

Repeat until zero

Jab tak num > 0 hai, loop chalta rahega.

Har step me ek digit extract hoga, reverse me add hoga, aur number chhota hota jayega.

Final reversed number

Jab num = 0 ho jata hai, loop rukta hai.

rev ke andar reversed number ready hota hai."""

# Check prime number  
n = int(input("Enter the number: "))

if n <= 1:
    print("Not a prime number.")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number.")
            break
    else:
        print("Prime number")

"""Step‑by‑Step Logic
Input number

User ek number enter karta hai → n.

Check <= 1

Agar n <= 1 hai to directly "Not a prime number" print hota hai.

Kyunki prime numbers hamesha greater than 1 hote hain.

Loop from 2 to n-1

For loop i ko 2 se lekar n-1 tak chalata hai.

Har i ke liye check hota hai ki n % i == 0 hai ya nahi.

Divisibility check

Agar koi i number ko divide kar deta hai (remainder 0), to wo prime nahi hai.

Print "Not a prime number" aur loop break ho jata hai.

Else with for loop

Python me for loop ke saath else ka matlab hai:

Agar loop normally complete ho gaya (break nahi hua), tabhi else chalega.

Matlab agar koi divisor nahi mila, to "Prime number" print hoga."""

# sum of digit
n = int(input("enter the number :"))
def sum_of_digit(n):
     total = 0
     while n>0:
          digit = n % 10
          total = total + digit
          n //= 10
     return total     
     
print(sum_of_digit(n))     

"""Workflow of Sum of Digits
Start with a number  
Example: n = 1234

Initialize sum = 0  
Ye variable har digit ka total store karega.

Extract last digit

Formula: digit = n % 10

For 1234 → digit = 4

Add digit to sum

sum = sum + digit

Now sum = 0 + 4 = 4

Remove last digit from number

Formula: n = n // 10

For 1234 → n = 123

Repeat steps 3–5

Next digit = 3 → sum = 7

Next digit = 2 → sum = 9

Next digit = 1 → sum = 10

Stop when number = 0

Loop ends. Final sum = 10"""

#Armstrong number  
num = int(input("enter the number :"))
sum_of_digit = 0
temp = num

while temp > 0:
     digit = temp % 10
     sum_of_digit += digit ** 3
     temp //= 10
     
if sum_of_digit == temp:
     print(num, "This number is Armstrong.")
else:
     print(num, "This number is not Armstrong.")

"""Workflow Explanation
Input number

User ek number enter karta hai.

Example: num = 153.

Initialize variables

sum_of_cubes = 0 → cubes ka total store karega.

temp = num → original number ko copy karte hain taaki loop me use ho.

Loop through digits

Jab tak temp > 0 hai, har digit nikalte rahenge.

Extract last digit

digit = temp % 10 → last digit milta hai.

Example: 153 → digit = 3.

Cube and add

sum_of_cubes += digit ** 3 → digit ka cube nikal ke sum me add karte hain.

Example: 
3
3
=
27
.

Remove last digit

temp //= 10 → last digit remove ho jata hai.

Example: 153 → 15.

Repeat steps 4–6

Digits: 3 → 5 → 1

Cubes: 27 + 125 + 1 = 153.

Final check

Agar sum_of_cubes == num → Armstrong number ✔

Otherwise → Not Armstrong ❌."""    

#Palindrome number  
num = int(input("enter the number :"))
temp = num
revers = 0

while temp > 0:
     digit = temp % 10
     revers = revers * 10 + digit
     temp //= 10
     
if num == revers:
     print(num, " this is palidrom.")
else:
     print(num, "this is not palidrom.")

"""Workflow (Logic)
Input number lo (e.g., 121).

Original number store karo (temp = num).

Reverse nikalna:

Digit = num % 10 (last digit).

Reverse = reverse * 10 + digit.

Number ko chhota karo → num //= 10.

Repeat until num = 0.

Compare: Agar reverse == original number → Palindrome ✔ else ❌."""     

#Factorial of a number  
def factorial(n):
     result = 1
     for i in range(1, n+1):
          result *= i
     return result

print(factorial(5))   

"""📌 Step‑by‑Step Logic
Initialize → result = 1

Loop → for i in range(1, n+1) → yaha loop 1 se 5 tak chalega (i = 1,2,3,4,5).

Inside loop → result *= 1

Matlab har step pe result = result × 1.

Lekin 1 se multiply karne par value kabhi change nahi hoti.

So result hamesha 1 hi rahega.

Return result → loop khatam hone ke baad result = 1."""

# Fibonacci series
def fabicon(n):
     a,b = 0,1
     for i in range(n):
          print(a, end=" ")
          a,b = b,a+b 
     
print(fabicon(5))   

"""📌 Workflow (Logic)
Initialize first two terms → a = 0, b = 1.

Loop n times → har step pe current number print karo.

Update values →

a = b

b = a + b (old values ke basis pe).

Repeat until n terms → series ready ho jaati hai."""
#Greatest Common Divisor (GCD)  
import math 

def gcd(a,b):
    return math.gcd(a,b)
     
print(gcd(12,18))    

"""📌 Step‑by‑Step Logic
List divisors of each number.

12 → 1, 2, 3, 4, 6, 12

18 → 1, 2, 3, 6, 9, 18

Find common divisors → 1, 2, 3, 6

Pick greatest → 6
👉 So GCD(12,18) = 6."""

#Greatest Common Divisor (GCD)  
import math 

def LCM(a,b):
     return abs(a*b) // math.gcd(a,b)
     
print(LCM(4,5))     
"""Step‑by‑Step Logic
List multiples of each number.

4 → 4, 8, 12, 16, …

6 → 6, 12, 18, …

Find common multiples → 12, 24, …

Pick smallest → 12.
👉 So LCM(4,6) = 12.

📌 Formula Method
LCM aur GCD (Greatest Common Divisor) ka relation hota hai:

𝐿
𝐶
𝑀
(
𝑎
,
𝑏
)
=
𝑎
×
𝑏
𝐺
𝐶
𝐷
(
𝑎
,
𝑏
)
Example:

a = 12, b = 15

GCD(12,15) = 3

LCM = (12 × 15) ÷ 3 = 60"""