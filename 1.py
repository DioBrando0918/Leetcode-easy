"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

"""
找出数组numbers中的两个数，它们的和为给定的一个数target，并返回这两个数的索引(不需要去重)
"""


# ------會出現死循環----------
# class Solution:
#     def twoSum(self, nums: list, target: int):
#         ans = []
#         for i in len(nums):
#             for j in range(len(nums)):
#                 if nums.index(i) != j and i + nums[j] == target:
#                     return [nums.index(i), j]
#
#
# sol = Solution().twoSum([3, 2, 4], 6)
# print(sol)

# ----------.index(i)時間複雜度為O(1))並不是他的問題------------
# class Solution:
#     def twoSum(self, nums: list, target: int):
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i != j and nums[i] + nums[j] == target:
#                     return [i, j]
#
#
# sol = Solution().twoSum([3, 2, 4], 6)
# print(sol)


#
# --------------final---------------
# class Solution:
#     def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
#         numMap = {}
#         for i in range(len(nums)):
#             if numMap.__contains__(target - nums[i]):  # target-9=x, x+9=target,x=7
#                 print(f"if{numMap}")
#                 return [numMap.get(target - nums[i]), i]  # get():返回指定鍵的值 target - num[i]與i
#             else:
#                 numMap[nums[i]] = i  # 可將num從list轉換成dictionary,且key為元素值,value為對應索引
#                 print(f"else{numMap}")
#
#
# sol = Solution().twoSum([2, 7, 11, 15], 9)
# print(sol)


# class Solution:
#     def twoSum(self, nums: "list[int]", target: "int") -> "list[int]":
#         numsmap = {}
#         for i in range(len(nums)):
#             if numsmap.__contains__(target - nums[i]):
#                 return [i, numsmap.get(target - nums[i])]
#             else:
#                 numsmap[nums[i]] = i
