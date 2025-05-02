class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        l=len(nums);m,m1=0,l;ie=list(range(l))
        ie.sort(key=lambda i: (nums[i],i))
        for i in ie:
            m=max(m,i-m1)
            m1=min(m1,i)
        return m