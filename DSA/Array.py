#Contains Duplicate
#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
class Solution:
    def hasDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Object create karo
solution = Solution()
print(solution.hasDuplicate([1,2,3,4]))  

# 1. Traversal (Har element ko visit karna)
arr = [1,2,3,4,5]

for num in arr:
     print(num, end=" ")
# Insertion & Deletion (Element add ya remove karna)     
arr = [1,2,3,4,5]

arr.insert(2,8)
arr.pop(1)
print(arr)

#3. Searching (Element ko dhoondna)
def Linear_search(arr, target):
     for i in range(len(arr)):
          if arr[i] == target:
               return i
     return -1   
     
array = [1,23,4,5]
result = Linear_search(array, 4)
print(result)

# 4. Sorting (Order mein arrange karna)
arr = [1,6,43,554,32,2]

arr.sort()    #acending order
arr.sort(reverse=True)  #descending order

#. Kadane’s Algorithm (Maximum Subarray Sum)
def max_subarray_sum(arr):
     max_current = max_gobal = arr[0]
     
     for i in range(1, len(arr)):
          max_current = max(arr[i], max_current + arr[i])
          if max_current > max_gobal:
               max_gobal = max_current
     
     return max_gobal  
     
print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))

#2. Two Pointer Approach
def reversed_arr(arr):
     left = 0
     right = len(arr)-1
     
     while left < right:
          arr[left], arr[right] = arr[right], arr[left]
          left += 1
          right-=1
          
     return arr
     
array = [5,3,2,6,43,6,1]

result = reversed_arr(array)
print(result)
