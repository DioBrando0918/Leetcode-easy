"""
給定一個表示為整數數組digits 的大整數，其中每個digits[i] 是整數的第i 個數字。數字按從左到右的順序從最高有效到最低有效排序。大整數不包含任何前導 0。
將大整數加一併返回結果數字數組。
"""


# ....也是頗簡單.........
class Solution:
    def plusOne(self, digits: "List[int]") -> "List[int]":
        string = str()
        for i in digits:
            string += str(i)
        int_sum = int(string) + 1
        return [int(j) for j in str(int_sum)]


sol = Solution().plusOne([9, 9])
print(sol)
