# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = ListNode(0)
        odd = ListNode(0)
        e, o = even,odd
        i=0
        while head:
            if i & 1 == 0:
                e.next = ListNode(head.val)
                e = e.next
            else:
                o.next = ListNode(head.val)
                o = o.next
            head = head.next
            i += 1
        e.next = odd.next
        return even.next