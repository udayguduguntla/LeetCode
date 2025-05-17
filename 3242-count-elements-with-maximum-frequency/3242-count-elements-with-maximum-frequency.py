class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in set(nums):
            d[i]=nums.count(i)
        m=max(d.values())
        return sum([i for i in d.values() if i==m])