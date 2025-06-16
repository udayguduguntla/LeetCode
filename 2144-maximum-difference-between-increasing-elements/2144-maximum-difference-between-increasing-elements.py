class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # m,flag=float('-inf'),False
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] < nums[j]:
        #             flag = True
        #             m=max(m,nums[j]-nums[i])
        # return m if flag else -1

        ans=-1
        min_value = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > min_value: ans=max(ans, nums[i]-min_value)
            else: min_value = nums[i]
        return ans