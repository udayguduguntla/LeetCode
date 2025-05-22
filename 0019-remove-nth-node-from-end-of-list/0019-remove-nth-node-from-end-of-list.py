# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def countList(self,head):
        cou=0
        p=head
        while p:
            cou+=1
            p=p.next
        return cou
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len=self.countList(head)
        if len==n:
            return head.next
        p=head
        for i in range(len-n-1):
            p=p.next
        if p.next:
            p.next=p.next.next
        return head