# 1 string method
number = "123"

reverse_string = number[::-1]

print(reverse_string)

# 2
number = input("enter the num :")

reverse_string = number[::-1]

if reverse_string == number:
     print("palidrome hai")
else:
     print("not palidrome")

# 1 integer method
number = int(input("enter the num :"))

original_number = number
reverse_number = 0

while number > 0:
     digit = number % 10
     reverse_number = reverse_number + digit
     number = number // 10
     
if original_number == reverse_number:
     print("Palindrome hai")
else:
     print("not Palindrome")
     

