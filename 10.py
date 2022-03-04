"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

給定一個整數數組 nums，找到總和最大的連續子數組（至少包含一個數）並返回它的總和。
子數組是數組的連續部分。
"""


class Solution:
    def maxSubArray(self, nums: 'list[int]') -> int:
        if not nums:
            return 0



sol = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(sol)
