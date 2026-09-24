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