def twosum(number, traget):
     left = 0
     right = len(number) - 1
     
     while left < right:
          current_sum = number[left] + number[right]
          
          if current_sum == traget:
               return [
                    left + 1,
                    right + 1,
               ]
          elif current_sum < traget:
               left += 1
          else:     
               right -= 1
     return []          
               
print(twosum([2,7,11,15], 9))      

"""Problem: Move Zeroes (In-Place Rearrangement)
Problem Statement:
Aapko ek integer array nums di gayi hai. Aapko saare 0s (zeros) ko array ke aakhri (end) mein shift karna hai, aur baaki non-zero numbers ka relative order (sequence) change nahi hona chahiye.

Constraint: Yeh kaam aapko bina koi extra array banaye (in-place) karna hai.

Example:
Input: nums = [0, 1, 0, 3, 12]

Output: [1, 3, 12, 0, 0]"""