import numpy as np
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(int(np.prod(nums[-3:])),(nums[0]*nums[1]*nums[-1]))