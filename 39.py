"""
Remove Linked List Elements
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""


# ----小姐姐寫的------------
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# dummy->head
# dummy->1->2->6->3->4->5->6
class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(None)
        dummy.next = head  # 後續return用
        previous = dummy  # 須從最前面開始
        current = dummy.next  # 第一個節點
        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = current
            current = current.next
        return dummy.next


head = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(6)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

sol = Solution().removeElements(head, 6)
