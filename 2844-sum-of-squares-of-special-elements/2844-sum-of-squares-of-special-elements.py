class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # return sum(nums[i]**2 for i in range(len(nums)) if len(nums) % (i+1) == 0)

        return sum(x**2 for i,x in enumerate(nums,start=1) if len(nums) % i == 0)