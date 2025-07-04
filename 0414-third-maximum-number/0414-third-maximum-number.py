class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) == 1:
            return nums[-1]
        if len(nums) < 3:
            return nums[1] if nums[1] > nums[0] else nums[0]
        a, b, c = float('-inf'),float('-inf'),float('-inf')
        for i in nums:
            if i > a:
                a, b, c = i,  a, b
            elif i > b:
                b, c = i, b
            elif i > c:
                c = i
        return(c)