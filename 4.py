"""
給定一個僅包含字符 '(', ')', '{', '}', '[' 和 ']' 的字符串 s，確定輸入字符串是否有效。

輸入字符串在以下情況下有效：

開括號必須用相同類型的括號閉合。
開括號必須以正確的順序閉合。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        left = "([{"
        stack = []  # 需要一進一出所以使用棧
        mp = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in left:  # 確認是不是左括號
                stack.append(i)
            else:
                if not stack or mp[i] != stack.pop():  # 如果棧為空或是右括號不等於左瓜號 則return False 棧為空是因為佐括號=右括號 然後又再進入一次此行 這時棧為空的話會娶不到值 才加一個not stack
                    return False
        if not stack:  # 若全部執行完 stack為空 代表
            return True


sol = Solution().isValid("()[]{}")
print(sol)
