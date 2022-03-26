"""
Reverse Bits

Reverse bits of a given 32 bits unsigned integer.
"""


# 給數字加上前綴'0b' 表示是二進制數字,python當中的十六進制和八進制數字的前綴分別為'0x' 和'0'
class Solution:
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans = (ans << 1) | (n & 1)
            n >>= 1
        return ans


sol = Solution().reverseBits(11111111111111111111111111111101)
print(sol)
