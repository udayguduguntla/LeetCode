class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        a=[]
        c=0
        for i in nums:
            if i!=0:
                a.append(i)
            else:
                c+=1
        a=a+[0]*c
        for i in range(len(nums)):
            nums[i]=a[i]