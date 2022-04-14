"""
Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head):
        



head = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)
n3 = ListNode(4)
n4 = ListNode(5)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

