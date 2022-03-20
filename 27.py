"""

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""


class Solution:
    def generate(self, numRows: 'int'):
        pascal_triangle = []
        for i in range(numRows+1):
            lst = [1 for i in range(i+1)]
            if len(lst) > 2:
                for j in range(len(lst)):
                    if 0 < j < len(lst)-1:
                        lst[j] = pascal_triangle[i-1][j-1]+pascal_triangle[i-1][j]
            pascal_triangle.append(lst)
        return pascal_triangle,pascal_triangle[numRows]

sol,sol1 = Solution().generate(5)
print(sol)
print(sol1)
