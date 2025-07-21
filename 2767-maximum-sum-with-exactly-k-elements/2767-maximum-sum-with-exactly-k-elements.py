class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return sum(range(max(nums),max(nums)+k))