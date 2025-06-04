class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # i,j=0,0
        # while i<len(nums):
        #     j+=1
        #     i+=2
        # l=[]
        # for i in range(n):
        #     l += [nums[i],nums[j]]
        #     j+=1
        # return l

        l=[]
        for i in range(n):
            l.extend([nums[i],nums[i+n]])
        return l