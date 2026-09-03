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