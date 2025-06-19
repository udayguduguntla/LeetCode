# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        while head and head.val in nums:  head = head.next
        ptr=head
        s = set(nums)
        while ptr and ptr.next:
            if ptr.next.val in s:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return head