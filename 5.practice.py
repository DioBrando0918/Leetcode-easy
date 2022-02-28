class ListNode:
    def __init__(self, val ):
        self.val = val
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(None)
        prev = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        if not l1:
            prev.next = l2
        elif not l2:
            prev.next = l1
        return dummy.next


# 先創節點 在用next做指標(箭頭)
head1 = ListNode(2)
n1 = ListNode(3)
n2 = ListNode(4)
n3 = ListNode(9)
head1.next = n1  # 如果用n1 = head.next, 因為head.next還是None所以要用haed.next = n1
n1.next = n2
n2.next = n3

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
