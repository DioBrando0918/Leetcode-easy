"""
Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""


class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
