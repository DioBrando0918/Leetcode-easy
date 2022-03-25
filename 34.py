"""
Excel Sheet Column Title
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
"""


# 數字轉字母 26進制的題
class Solution:
    def convertToTitle(self, columNumber: 'int'):
        result, num = "", columNumber
        while num:
            result += chr((num - 1) % 26 + ord('A'))
            num = (num - 1) // 26
        return result[::-1]


sol = Solution().convertToTitle(30)
print(sol)
