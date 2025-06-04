class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in set(nums1+nums2):
            if i in nums1 and i in nums2:
                l.extend([i]*min(nums1.count(i) , nums2.count(i)))
        return l