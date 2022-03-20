"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""


# --worte it myself ,效率較低------
class Solution:
    def generate(self, numRows: 'int'):
        pascal_triangle = []
        for i in range(numRows):
            lst = [1 for i in range(i + 1)]
            if len(lst) > 2:
                for j in range(len(lst)):
                    if 0 < j < len(lst) - 1:
                        lst[j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
            pascal_triangle.append(lst)
        return pascal_triangle


# --其他人的解,比較優美空間複雜度較低,他把限制直接加在range()裡,並且直接對建好的列表進行修改 而不是修改好在append
# class Solution(object):
#     def generate(self, numRows):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """
#         res = [[1] * i for i in range(1, numRows + 1)]
#         for i in range(2, numRows):
#             for j in range(1, i):
#                 res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
#         return res


sol = Solution().generate(5)
print(sol)
