class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0 or target not in nums:
            return [-1,-1]
        l=[]
        for i in range(len(nums)):
            if nums[i] == target:
                l.append(i)
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == target:
                l.append(i)
                break
        return l