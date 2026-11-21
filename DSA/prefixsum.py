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
print(range_sum(1,3))    # 14 - 4 = 10
print(range_sum(0, 4))  # 19 - 0 = 19

"""Question: Subarray Sum Equals K
Tumhe ek integer array nums (jisme positive, negative, ya 0 ho sakte hain) aur ek integer k diya gaya hai.
Tumhe batana hai ki aise kitne continuous subarrays hain jinka sum exact k ke barabar ho."""
def subarray_sum_k(nums: list[int], k: int) -> int:
     freq = {0: 1}
     current_sum = 0
     count = 0

     for num in nums:
          current_sum += num
          target = current_sum - k 

          if target in freq:
               count += freq[target]
          freq[current_sum] = freq.get(current_sum, 0) + 1
     return count     