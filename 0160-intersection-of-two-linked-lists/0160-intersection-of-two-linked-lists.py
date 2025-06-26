# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        l1, l2 = headA, headB
        while l1:
            visited.add(l1)
            l1 = l1.next
        while l2:
            if l2 in visited:
                return l2
            l2 = l2.next
        return None