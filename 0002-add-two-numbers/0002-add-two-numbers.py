# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: list, l2: list) -> Optional[ListNode]:
        n=ListNode(0)
        cur=n
        c=0
        while l1 or l2 or c:
            val=(l1.val if l1 else 0) + (l2.val if l2 else 0) + c
            c=val//10
            cur.next=ListNode(val%10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return n.next