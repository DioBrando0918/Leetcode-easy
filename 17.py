"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
給定root二叉樹的 ，返回其節點值的中序遍歷。
"""


def inorderTraversal(self, root: 'Optional[TreeNode]') -> 'List[int]':
    if self.root is None:
        return []
    return self.inorderTraversal(self.root.left) + [self.root.val] + self.inorderTraversal(self.root.right)

