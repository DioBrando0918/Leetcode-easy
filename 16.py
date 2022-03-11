"""
給定排序鍊錶的頭部，刪除所有重複項，使每個元素只出現一次。返回排序好的鍊錶。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: 'Optional:[ListNode]') -> 'Optional:[ListNode]':
        current = head
        while current:
            while current.next and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        return head


head = ListNode(1)
n1 = ListNode(1)
n2 = ListNode(2)
head.next = n1
n1.next = n2
sol = Solution().deleteDuplicatesP(head)
print(sol)

while sol:
    print(sol.val)
    sol = sol.next
