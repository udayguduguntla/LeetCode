class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans, res = [0]*len(nums), 0
        for i in range(len(nums)):
            ans[i] = ans[i//2] + (i & 1)
            if ans[i] == k:  res += nums[i]
        return res