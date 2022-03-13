"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        def to_bst(nums, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = to_bst(nums, start, mid - 1)
            node.right = to_bst(nums, mid + 1, end)
            return node

        return to_bst(nums, 0, len(nums) - 1)
