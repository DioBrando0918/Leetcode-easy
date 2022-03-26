"""
Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

# ---wrote it myself,time complexity and space complexity are both lower-----
# class Solution:
#     def isHappy(self, n: 'int'):
#         self.map = {}
#         return self.calculate(n)
#
#     def calculate(self, n):
#         ans = 0
#         if n == 1:
#             return True
#         for i in str(n):
#             ans += eval("pow(int(i),2)")
#         if self.map.__contains__(ans):
#             return False
#         self.map[ans] = ans
#         return self.calculate(ans)


# 別人的解,快很多,空間複雜度也低
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         cycle_members = [n]
#
#         while (n != 1):
#             digit = [int(d) for d in str(n)]
#             temp_n = 0
#             for i in range(len(digit)):
#                 temp_n = digit[i] ** 2 + temp_n
#             n = temp_n
#             cycle_members_set = set(cycle_members)
#             if n != 1 and (n in cycle_members_set):
#                 return False
#
#             cycle_members.append(n)
#
#         return True

sol = Solution().isHappy(2000)
print(sol)
