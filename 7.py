"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
Since it is impossible to change the length of the array in some languages, you mus instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

题意为给你一个数组，再给你一个值，删除所有和这个值相等的元素，返回新列表的长度，要求不能在使用额外的数组，只能操作这一个数组。
"""


# remove()無法全部移除,會留下一個
class Solution:
    def removeElement(self, nums: 'list[int]', val: 'int') -> int:
        length = len(nums)
        x = 0
        while x < length:
            if nums[x] == val:
                nums.remove(val)
                x -= 1  # index0 被移掉的話 後面的1會往前推 所以x要-=1後面在加回來
                length -= 1  # 因為remove掉一個 所以-1 否則會超出索引error
            x += 1  # 要加1才能繼續取新的索引值
        return len(nums)


sol = Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
print(sol)
