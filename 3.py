"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

編寫一個函數來查找字符串數組中最長的公共前綴字符串。
如果沒有公共前綴，則返回一個空字符串“”。
"""


class Solution:
    def longestCommonPrefix(self, strs: "list[str]") -> str:
        if not strs:
            return ""
        min_l = min(map(len, strs))
        index = 0

        for i in range(len(strs)):
            for j in range(len(strs)):
                if index < len(strs)-1:
                    if strs[index][:min_l] == strs[index+1][:min_l]:
                        index += 1
                    else:
                        min_l -= 1
        return strs[0][:min_l]


sol = Solution().longestCommonPrefix(["flower","fkow"])
print(sol)
