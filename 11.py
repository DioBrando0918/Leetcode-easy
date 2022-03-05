"""
給定一個由一些單詞組成的字符串 s 由一些空格分隔，返回字符串中最後一個單詞的長度。
單詞是僅由非空格字符組成的最大子串。
"""


# .....雞巴太簡單...--------------------------
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strs = s.split()
        return len(strs[-1])
