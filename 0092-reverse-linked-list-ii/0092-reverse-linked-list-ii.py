# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:   return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for i in range(left - 1):
            prev = prev.next
        
        curr = prev.next
        rev = None
        
        for i in range(right - left + 1):
            nxt = curr.next
            curr.next = rev
            rev = curr
            curr = nxt
        prev.next.next = curr
        prev.next = rev
        
        return dummy.next