"""
Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""


class Solution:
    def postorderTraversal(self, root):
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
