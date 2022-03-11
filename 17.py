"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
給定root二叉樹的 ，返回其節點值的中序遍歷。
"""


class Solution:
    def inorderTraversal(self, root: 'Optional[TreeNode]') -> 'List[int]':
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)



