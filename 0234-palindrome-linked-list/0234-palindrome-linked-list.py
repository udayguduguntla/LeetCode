# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        if head == None or head.next == None:
            return True
        l=[]
        while fast != None and fast.next != None:
            l.append(slow.val)
            slow=slow.next
            fast=fast.next.next
        if fast!=None:
            slow=slow.next
        while slow != None:
            if l.pop() != slow.val:
                return False
            slow=slow.next
        return True