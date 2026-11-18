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

  # 1. Pehli window (0 se k-1 tak) ka sum nikalo
  for i in range(k):
    window_sum += arr[i]

  # Sahi tarika: Seedha max_sum ko window_sum ke barabar kar do
  max_sum = window_sum

  # 2. Window ko aage slide karo
  for i in range(k, n):
    window_sum = window_sum + arr[i] - arr[i - k]
    max_sum = max(max_sum, window_sum)

  return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3
print(maxSumSubarray(arr, k))  # Output: 9

"""📝 Problem: Longest Substring Without Repeating Characters
Problem Statement:
Aapko ek string s di gayi hai. Aapko ek aisi sabse lambi substring ki length find karni hai
jisme koi bhi character repeat na hota ho (yani saare characters unique hon)."""
def lengthOfLongestSubstring(s: str) -> int:
     char_set = set()
     left = 0
     max_len = 0

     for right in range(len(s)):
          while s[right] in char_set:
               char_set.remove(s[left])
               left += 1
          char_set.add(s[right])
          
          max_len = max(max_len, right - left + 1)
     return max_len     
print(lengthOfLongestSubstring('abcabcbb'))  # Output: 3 ("abc")
print(lengthOfLongestSubstring('bbbbb'))  # Output: 1 ("b")
print(lengthOfLongestSubstring('pwwkew'))  # Output: 3 ("wke")