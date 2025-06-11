class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # a = sorted(set(nums1 + nums2) - set(nums1).symmetric_difference(set(nums2)))
        # return a[0] if a else -1

        a=sorted(set(nums1) & set(nums2))
        return a[0] if a else -1