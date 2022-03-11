"""
給定一個非負整數 x，計算並返回 x 的平方根。
由於返回類型是整數，所以十進制數字被截斷，只返回結果的整數部分。
注意：您不能使用任何內置的指數函數或運算符，例如 pow(x, 0.5) 或 x ** 0.5。
"""

#------暴力解-----------------
class Solution:
    def mySqrt(self, x: 'int') -> int:
        if x <= 1:
            return x
        s = 1
        while True:
            if s * s > x:
                return s - 1
            s += 1




sol = Solution().mySqrt(4)
print(sol)