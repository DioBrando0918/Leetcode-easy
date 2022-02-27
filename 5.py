"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

給你兩個排序的鍊錶list1 和list2 的頭。
將兩個列表合併到一個排序列表中。該列表應通過將前兩個列表的節點拼接在一起來製作。
返回合併鍊錶的頭部。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
            # 比较l1和l2的值的大小
        if l1.val < l2.val:
            # 将l2递归到l1上
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            # 将l1递归到l2上
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2


# 有序鍊表1
head1 = ListNode(2)
n1 = ListNode(3)
n2 = ListNode(4)
n3 = ListNode(9)
head1.next = n1
n1.next = n2
n2.next = n3

# 有序鍊表2
head2 = ListNode(3)
m1 = ListNode(5)
m2 = ListNode(7)
m3 = ListNode(8)
head2.next = m1
m1.next = m2
m2.next = m3

sol = Solution()
res = sol.mergeTwoLists(head1, head2)
while res:
    print(res.val)
    res = res.next
