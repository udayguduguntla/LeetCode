# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        # approach - 1
        # p=head
        # l=[]
        # while p != None:
        #     if p.next in l:
        #         return True
        #     l.append(p)
        #     p=p.next
        # return False

        # approach - 2

        s = set()
        while head:
            if head in s:   return True
            s.add(head)
            head=head.next
        return False