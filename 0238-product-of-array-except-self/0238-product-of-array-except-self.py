import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 not in nums:
            m=np.prod(nums)
            return [int(m//i) for i in nums]
        else:
            l=[1]*len(nums)
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if j==i:
                        continue
                    l[i]*=nums[j]
            return l