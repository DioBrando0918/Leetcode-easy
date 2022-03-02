"""
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

返回 haystack 中第一次出現 needle 的索引，如果 needle 不是 haystack 的一部分，則返回 -1。

澄清：
當 needle 為空字符串時，我們應該返回什麼？這是面試時問的好問題。
為了解決這個問題，當 needle 為空字符串時，我們將返回 0。這與 C 的 strstr() 和 Java 的 indexOf() 一致。
"""


# ----自己寫的能過,效率較低----------
# class Solution:
#     def strStr(self, haystack: 'str', needle: 'str') -> int:
#         if not needle:
#             return 0
#         elif needle not in haystack:
#             return -1
#         needle_len = len(needle)
#         # print(f"neddle_length:{needle_len}")
#         haystack_len = len(haystack)
#         # print(f"haystack_len:{haystack_len}")
#         min_length = 0
#         max_length = needle_len - min_length  # max_lenth長度固定 但在遍歷中因索引值會一直往後 所以要改用方程
#         count = 0 #計數
#
#         while count <= haystack_len:
#             # print(haystack[min_length:max_length])
#             if haystack[min_length:max_length] == needle:
#                 return min_length
#             else:
#                 min_length += 1
#                 max_length += 1
#                 count += 1

# --------別人寫的 不用while迴圈 try except time complexity為O(n)(?)-------
class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> int:
        try:
            return haystack.index(needle)  # 如果needle是空字串會回傳0  找到架設索引大於一個 會回傳最小索引值
        except:
            return -1


sol = Solution().strStr("hello", "lo")
print(sol)
