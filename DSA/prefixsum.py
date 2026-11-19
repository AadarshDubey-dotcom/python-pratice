"""Prefix sum ka matlab hota hai running total — yaani array ke starting se leke har
index tak ke saare elements ka jod (sum) pehle se nikal kar rakh lena.Isse fayda yeh hota hai
ki agar koi beech ke kisi hisse (range) ka sum pooche, toh baar-baar for loop chala kar elements
add nahi karne padte — seedha ek subtraction se $O(1)$ time mein answer mil jaata hai.:"""
num = [4,2,7,1,5]
prefix = [0] * (len(num) + 1)
for i in range(len(num)):
     prefix[i + 1] = prefix[i] + num[i]
def range_sum(left, right):
     return prefix[right + 1] - prefix[left]     
print(range_sum(1,3))    
print(range_sum(1,4))
