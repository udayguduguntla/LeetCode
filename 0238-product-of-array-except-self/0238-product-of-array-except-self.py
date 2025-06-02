from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 not in nums:
            m=reduce(lambda x,y: x*y,nums,1)
            for i in range(len(nums)):
                nums[i] = m//nums[i]
            return nums
        else:
            if nums.count(0) > 1:
                return [0]*len(nums)
            else:
                l=[]
                for i in range(len(nums)):
                    if nums[i]!=0:
                        l.append(0)
                    else:
                        l.append(reduce(lambda x,y : x*y,nums[:i]+nums[i+1:],1))
                return l