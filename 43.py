"""
Contains Duplicate II

Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""


# ----worte it myself---so easy
class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: 'int'):
        map = {}
        for i in range(len(nums)):
            if map.__contains__(nums[i]):
                absolute = abs(i - map[nums[i]])
                if absolute <= k:
                    return True
            map[nums[i]] = i
        return False


sol = Solution().containsNearbyDuplicate([1, 2, 3, 1], 3)
print(sol)
