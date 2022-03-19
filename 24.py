"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
一個短語是回文，如果在將所有大寫字母轉換為小寫字母並刪除所有非字母數字字符後，它向前和向後讀取相同。字母數字字符包括字母和數字。

給定一個字符串s，true如果它是回文則返回，false否則返回。
"""


# -----wrote it myself--------
class Solution:
    def isPalindrome(self, strs):
        strs = strs.lower()
        print(strs)
        string = [i for i in strs if 'a' <= i <= 'z' or '0' <= i <= '9']
        string = ''.join(string)  # 記住join()用法
        if string == string[::-1]:
            return True


sol = Solution().isPalindrome("A man, a plan, a canal: Panama")
print(sol)
