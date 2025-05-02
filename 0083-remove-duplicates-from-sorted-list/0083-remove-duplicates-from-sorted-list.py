# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:    return None
        p=head;l=[p.val]
        while p.next != None:
            if p.next.val in l: p.next=p.next.next
            else:   l.append(p.next.val);p=p.next
        return head