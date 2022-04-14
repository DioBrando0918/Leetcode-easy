"""
Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""


# ---worte it myself ,error-------
# class Solution:
#     def isIsomorphic(self, s: 'str', t: 'str'):
#         map1 = {}
#         for i in range(len(s)):
#             if map1.__contains__(s[i]) and t[i] != map1[s[i]]:
#                 return False
#             else:
#                 map1[s[i]] = t[i]
#                 print(map1)
#         mapval = [map1[k] for k in map1]
#         return len(map1) == set(mapval)

# -----別人的解-------------
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        for i in range(len(s)):
            # 為了不被相同的key覆蓋
            if s[i] not in hashmap:
                hashmap[s[i]] = t[i]
            # 判斷是否一個字符映射到兩個字符
            elif hashmap[s[i]] != t[i]:
                return False
        print(hashmap)
        mapval = [hashmap[k] for k in hashmap]  # 判斷不同的字符映射到相同的字符”这一情况
        # 使用列表推導式:mpval = ['b', 'a', 'b', 'a'],是將hashmap每一個value製作成列表
        return len(mapval) == len(set(mapval))  # 對['b', 'a', 'b', 'a']使用set()會輸出{'b', 'a'}


sol = Solution().isIsomorphic("badc", "baba")
print(sol)
