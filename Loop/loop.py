#Write a loop that prints numbers from 1 to 10.
for i in range(1, 11):
     print(i)

#Input: N = 5 → Output: 15 (1+2+3+4+5).
n = int(input("enter the number:"))
sum = 0
for i in range(1, n+1):
     sum += i
print("Sum =", sum)     

#Print the table of n using a loop.
n = int(input("Entert the number :"))

for i in range(1,11):
     print(n*i)

#Reverse an array  
arr = [1,2,3,4,5]
arv = []

for i in range(len(arr)-1, -1,-1):
     print(arr[i])