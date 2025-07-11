class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        duplicate = -1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                duplicate = nums[i]
                break
        missing = set(range(1,len(nums)+1)) ^ set(nums)
        return [duplicate, missing.pop()]