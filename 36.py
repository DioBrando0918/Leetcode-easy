"""
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
"""


# ----WROTE IT MYSELF , 前2位可以 後面就不行了....----
# class Solution:
#     def titleToNumber(self, columnTitle: str) -> int:
#         """
#         A -> 1
#         B -> 2
#         C -> 3
#         ...
#         Z -> 26
#         AA -> 27
#         AB -> 28
#         ...
#         """
#         ans = 0
#         for i in columnTitle:
#             if i == columnTitle[-1]:
#                 ans += ord(i) % ord('A') + 1
#             else:
#                 ans += ((ord(i) + 1) % ord('A')) * 26
#         return ans


# ----進位用乘的,不是用加的,低能兒-----------
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in columnTitle:
            result *= 26
            result += ord(i) - ord('A') + 1

        return result


sol = Solution().titleToNumber("ZAB")
print(sol)
