"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


# class Solution:
#     def singleNumber(self, nums: 'List'):
#         nums = set(nums)
#         dic = {}
#         for i in nums:
#             dic[i] += 1
#         return dic.items(1)
#
# sol = Solution().singleNumber([4,2,2,3,1])
# print(sol)

# -----能過,時間太長效率太短------
# class Solution:
#     def singleNumber(self, nums: 'Lsit[int]'):
#
#         for i in nums:
#             if nums.count(i) == 1:
#                 return int(i)

#
# sol = Solution().singleNumber([4, 2, 2, 3, 1])
# print(sol)


# ------互斥或閘,同樣的會消掉------
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res


sol = Solution().singleNumber([2, 4, 3, 1, 5])
sol1 = Solution().singleNumber([4, 1, 2, 4, 1])

print(sol)
