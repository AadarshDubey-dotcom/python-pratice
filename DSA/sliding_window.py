"""📝 Problem: Maximum Sum Subarray of Size $K$ (Fixed Window)Problem Statement:
Aapko ek integer array arr aur ek integer k diya gaya hai.
Aapko ek aisi contiguous subarray dhundhni hai jiski size exact k ho,
aur uska sum maximum (sabse bada) ho. Woh maximum sum return karna hai."""
"""Example:
Input: arr = [2, 1, 5, 1, 3, 2], k = 3

Output: 9

Explanation: Subarray of size 3 with maximum sum is [5, 1, 3], aur inka sum 5 + 1 + 3 = 9 hota hai."""
def maxSumSubarray(arr, k):
     n = len(arr)
     if k > n:
          return -1
    
    window_sum = 0
    max_sum = 0

    for i in range(k):
          window_sum += arr[i]
     
     max_sum = window_sum += arr[i]