"""

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


# ---BFS---wrote it myself --------
# # ----應該能過....超過時間---------
# class Solution:
#     def maxProfit(self, prices: 'List[int]'):
#         non_decrease = sorted(prices) #要用sorted才會返回新列表,sort()無返回值
#         ans = []
#         for i in non_decrease:
#             for j in range(len(prices)):
#                 if prices[j] - i > 0 and j > prices.index(i):
#                     ans.append(prices[j] - i)
#         if ans:
#             return max(ans)
#         else:
#             return 0
#
#
# sol = Solution().maxProfit( [7,1,5,3,6,4])
# print(sol)


# ------正解,time complexity is O(n)---------
class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        profit = 0
        low = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                profit = max(prices[i] - low, profit)
        return profit
