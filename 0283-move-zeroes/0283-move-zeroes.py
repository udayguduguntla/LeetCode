class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # a=[]
        # c=0
        # for i in nums:
        #     if i!=0:
        #         a.append(i)
        #     else:
        #         c+=1
        # for i in range(c):
        #     a.append(0)
        # for i in range(len(nums)):
        #     nums[i]=a[i]

        # approch - 2
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        