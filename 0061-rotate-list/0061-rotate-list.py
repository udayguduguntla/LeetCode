# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def cot(self,head):
        p=head
        c=0
        while p!=None:
            c+=1
            p=p.next
        return c
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        c=self.cot(head)
        k=k%c
        if k==0:
            return head
        fast=slow=head
        for _ in range(k):
            fast=fast.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        new=slow.next
        slow.next=None
        fast.next=head
        return new