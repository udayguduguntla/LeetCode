class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # i,j,m,iterator=0,1,float('-inf'),0
        # while i<len(nums) and j<len(nums):
        #     if iterator & 1 == 0:
        #         print(nums[j],nums[i],nums[j]-nums[i],iterator,'even')
        #         m=max(m,nums[j]-nums[i])
        #         i+=2
        #     else:
        #         print(nums[i],nums[j],nums[i]-nums[j],iterator,'odd')
        #         m=max(m,nums[i]-nums[j])
        #         j+=2
        #     iterator +=1
        # return m

        m,flag=float('-inf'),False
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    flag = True
                    m=max(m,nums[j]-nums[i])
        return m if flag else -1