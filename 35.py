"""
Majority Element


Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


"""


# -----wrote it myself---------
# 能過runcode,過不了submit,時間複雜度太高,count時間複雜度為O(n),這樣整體時間複雜度為n^2
# class Solution:
#     def majorityElement(self, nums: 'List[int]'):
#         majority_length = len(nums)
#         majority_time = majority_length / 2
#         for i in nums:
#             if nums.count(i) > majority_time:
#                 return i


# wrote it myself,用字典推導式可以將時間複雜度降至O(n)
class Solution:
    def majorityElement(self, nums: 'List[int]'):
        count = 0
        map = {k: 0 for k in nums}
        majority_length = len(nums)
        majority_time = majority_length / 2
        for i in nums:
            map[i] += 1
            if map.get(i) > majority_time:
                return i


sol = Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])
print(sol)
