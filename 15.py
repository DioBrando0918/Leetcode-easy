"""
你正在爬樓梯。到達頂峰需要 n 步。
每次您可以爬 1 或 2 級台階。有多少種不同的方式可以爬到頂峰
"""


# ----wrote it myself ,透過動態規劃將大問題分成多個子問題
class Solution:
    def climbStairs(self, n: 'int') -> int:
        count = 2
        steps = [1, 2]  # index0 1種方式 index1 2種方式
        ans = 0
        while count < n:
            ans = (steps[count - 1] + steps[count - 2])
            steps.append(ans)
            count += 1
        return steps[n - 1]


sol = Solution().climbStairs(1)
print(sol)
