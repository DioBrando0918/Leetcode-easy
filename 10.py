"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

給定一個整數數組 nums，找到總和最大的連續子數組（至少包含一個數）並返回它的總和。
子數組是數組的連續部分。
"""


# ----wrote it myself,the time complexity is O(log(n^2),will show "Time Limit Exceeded")QQ----------
# class Solution:
#     def maxSubArray(self, nums: 'list[int]') -> int:
#         length_num = len(nums)
#         list_ans = []
#         if length_num == 1:
#             return nums[0]
#         for i in range(length_num):  # 第幾個元素開始加
#             ans = 0
#             for j in range(i, length_num):  # 從第i個元素一直往後加
#                 list_ans.append(nums[j])
#                 ans += nums[j]
#                 if ans >= nums[j]:  # 有可能加總完比num[j]還小 所以要取條件再append
#                     list_ans.append(ans)
#         if list_ans:
#             return max(list_ans)
#         else:
#             return max(nums)  # 有可能line22沒觸發 list_ans為空 所以答案是輸入列表最大值 例[-2-1]

# -----正解--------------
# class Solution:
#     def maxSubArray(self, nums):
#         """
#         计算列表中连续子数组的最大和
#         :param nums: list[int]
#         :return: int
#         """
#         if not nums:
#             return 0
#         cur_sum = nums[0]
#         max_sum = nums[0]
#         for i in nums[1:]:
#             # 计算当前的和与i相加之后的和比较的最大值
#             cur_sum = max(i, cur_sum + i)  # 如果加完新元素比原本還小 那要他幹嘛?
#             # 计算当前和与最大和比较的最大值
#             max_sum = max(max_sum, cur_sum)
#             # 沒取max會是全部列表i+到最後的最大值 取了之後會是i+到第n個元素的最大值 因為cur_sum不一定是最大值 需要max_sum來比較才能確定 例如到index6 的1加總玩是6 但是繼續到index8的話加總會是5
#             # 也許加完下一個index的值後會比較小 但是加到後面會比現在大 所以需要max_sum來儲存最大值 來確保可以吃到最大值 例如下一個元素是-5 肯定會變下 但是再一個是20 絕對會變大 所以需要max_sum
#             # max_sum是用來確保整個列表加總到哪裡是最大值 cur_sum是確保加完之後部會比index i還小
#         return cur_sum


class Solution:
    def maxSubArray(self, nums: 'List[int]') -> int:
        if not nums:
            return 0
        cur_sum = nums[0]
        max_sum = nums[0]
        for i in nums[1:]:
            cur_sum=max(i,cur_sum+i)
            max_sum = max(cur_sum,max_sum)
        return max_sum


sol = Solution().maxSubArray(
    [-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(sol)
