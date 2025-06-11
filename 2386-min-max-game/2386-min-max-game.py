class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        # while len(nums) != 1:
        #     l=[]
        #     for i in range(len(nums)//2):
        #         if i & 1 == 0:
        #             l.append(min(nums[2 * i], nums[2 * i + 1]))
        #         else:
        #             l.append(max(nums[2 * i], nums[2 * i + 1]))
        #     nums=l
        # return nums[0]

        # approach -2

        if len(nums) == 1:
            return nums[0]
        l=[]
        for i in range(len(nums)//2):
            if i & 1 == 0:
                l.append(min(nums[2 * i], nums[2 * i + 1]))
            else:
                l.append(max(nums[2 * i], nums[2 * i + 1]))
        return self.minMaxGame(l)