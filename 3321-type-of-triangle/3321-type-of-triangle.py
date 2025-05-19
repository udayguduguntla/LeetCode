class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums.count(nums[0]) == 3:
            return "equilateral"
        elif (nums[0]+nums[1]>nums[2] and nums[2]+nums[1]>nums[0] and nums[0]+nums[2]>nums[1]):
            if nums.count(nums[0]) == 2 or nums.count(nums[1]) == 2:
                return "isosceles"
            elif nums[0]!=nums[1]!=nums[2]:
                return "scalene"
        else:
            return "none"