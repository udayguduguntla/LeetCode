class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums += [nums[0]]
        return max(abs(nums[i] - nums[i+1]) for i in range(len(nums)-1))