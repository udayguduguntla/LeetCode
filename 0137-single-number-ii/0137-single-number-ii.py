class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # s=set()
        # for i in range(len(nums)):
        #     if nums[i] not in s:
        #         for j in range(i+1,len(nums)):
        #             if nums[i]^nums[j] == 0:
        #                 s.add(nums[i])
        #                 break
        #         else:
        #             return nums[i]

        # approach - 2

        ones = 0
        twos = 0
        for i in nums:
            ones = (ones ^ i) & ~twos
            twos = (twos ^ i) & ~ones
        return ones