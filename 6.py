"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

給定一個按非遞減順序排序的整數數組 nums，就地刪除重複項，使每個唯一元素只出現一次。元素的相對順序應保持不變。
由於在某些語言中無法更改數組的長度，因此您必須將結果放在數組 nums的第一部分。更正式地說，如果刪除重複項後有 k個元素，則 nums的前 k個元素應該保存最終結果。在前 k個元素之外留下什麼並不重要。
將最終結果放入 nums的前 k個槽後返回 k。
不要為另一個數組分配額外的空間。您必須通過使用 O(1)額外內存就地修改輸入數組來做到這一點。
"""


# -------自己寫的 會抱錯-------正解-------------------
# class Solution:
#     def removeDuplicates(self, nums: 'List[int]') -> int:
#         if not nums:
#             return 0
#         length = len(nums)
#         new_length = 0
#         for i in range(1, length):
#             if nums[i] != nums[i - 1]:
#                 new_length += 1
#                 nums[i - 1] = nums[i]
#         return new_length + 1

# --------也抱錯---------------
# class Solution:
#     def removeDuplicates(self, nums: 'List[int]') -> int:
#         if not nums:
#             return 0
#
#         for i in range(len(nums)):
#             if i < len(nums) - 1:
#                 if nums[i] == nums[i + 1]:
#                     nums.remove(nums[i + 1])
#         print(nums)
#         for j in range(len(nums)):
#             if j < len(nums) -1:
#                 if nums[j] == nums[j + 1]:
#                     nums.remove(nums[j + 1])
# ---------------正解-------------------
class Solution:
    def removeDuplicates(self, nums):
        '''
        :param nums: list[int]
        :return:int
                '''
        # 如果数组为空，则返回0
        if not nums:
            return 0
        new_length = 0
        length = len(nums)
        # 从1到n-1开始循环遍历
        for i in range(1, length):
            # 如果i不等于nums[now_length](其实是i-1)
            if nums[i] != nums[new_length]:
                new_length += 1
                nums[new_length] = nums[i]
        return new_length + 1


sol = Solution().removeDuplicates([0, 0, 0, 0, 0])
print(sol)
