"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

給定一個由不同整數組成的排序數組和一個目標值，如果找到目標，則返回索引。如果不是，則返回按順序插入的索引。
您必須編寫一個具有 O(log n) 運行時復雜度的算法。
"""


# worte it myself ,因題目規定time complexity is O(logn),所以用try except不行
# class Solution:
#     def searchInsert(self, nums: "list[int]", target: int) -> int:
#         count = 0
#         length_nums = len(nums)
#         if target == 0:
#             return 0
#         elif target in nums:  # .index()裡沒有target的值 會抱錯
#             return nums.index(target)
#         else:
#             while count < length_nums:
#                 # print(length_nums)
#                 # print(count)
#                 if length_nums == 1 :
#                     if target<= nums[length_nums]
#                 if nums[count] <= target <= nums[count + 1]:
#                     nums.insert(count + 1, target)
#                     return count + 1
#                 elif target > max(nums):
#                     nums.append(target)
#                     return length_nums
#                 count += 1

# ------wrote it myself----------
class Solution:
    def searchInsert(self, nums: 'list[int]', target: 'int') -> int:
        length_nums = len(nums)
        count = 1
        if target in nums:
            return nums.index(target)
        while target not in nums:
            nums.append(target)
            nums.sort()
            return nums.index(target)


sol = Solution().searchInsert([1, 3, 5, 6], 7)
print(sol)
