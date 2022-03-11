"""
Given two binary strings a and b, return their sum as a binary string.
給定兩個二進製字符串 a 和 b，將它們的和作為二進製字符串返回。
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:  # int預設輸出是進制,第二項參數要先選擇輸入是幾進制,在用bin轉換為十進制,輸出會是0b....所以要索引[2:]
        return bin(int(a, 2) + int(b, 2))[2:]


sol = Solution().addBinary('11', '1')
