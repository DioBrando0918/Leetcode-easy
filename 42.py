"""
Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""


# ----想也知道會超時----------
# class Solution:
#     def containsDuplicate(self, nums: 'List[int]'):
#         for i in nums:
#             if nums.count(i) > 1:
#                 return True
#         return False


# ----wrote it my self ------------
class Solution:
    def containsDuplicate(self, nums: 'List[int]'):
        map = {}
        for i in range(len(nums)):
            if map.__contains__(nums[i]):  # conrains 是找key不是value
                return True
            map[nums[i]] = i
        return False


sol = Solution().containsDuplicate([1, 2, 3, 4])
print(sol)
