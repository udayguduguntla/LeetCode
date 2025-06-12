class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums*2
        
        # approach - 2
        n=len(nums)
        ans = [0]*2*n
        i,j=0,n
        for i in range(n):
            ans[i]=ans[i+n]=nums[i]
        return ans