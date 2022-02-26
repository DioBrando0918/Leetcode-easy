"""
給定一個整數 x，如果 x 是回文整數，則返回 true。
當一個整數向後讀和向前讀一樣時，它就是一個回文數。
例如，121 是回文，而 123 不是。
"""


class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            if x == int(str(x)[::-1]):
                return True
            return False


sol = Solution().isPalindrome(x=10)  # 類別記得加括號...不然會報參數錯誤
print(sol)
