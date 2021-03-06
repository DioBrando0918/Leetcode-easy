"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: 'Optional[TreeNode]'):
        if root is None:
            return 0
        return abs((1+self.isBalanced(root.left))-(1+self.isBalanced(root.right)))
