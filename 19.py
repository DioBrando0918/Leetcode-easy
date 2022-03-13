"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True  # 若樹為空 本身就是對稱的
        return self.isSymmetricRecu(root.left, root.right)

    def isSymmetricRecu(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)
