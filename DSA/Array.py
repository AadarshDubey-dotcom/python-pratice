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
