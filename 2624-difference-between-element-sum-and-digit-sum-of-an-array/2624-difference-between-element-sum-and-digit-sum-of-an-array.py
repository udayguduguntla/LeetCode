class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        # return abs(sum(nums) - sum(int(i) for i in "".join(list(map(str,nums)))))

        # approach - 2

        def sumOfDigits(n):
            s=0
            while n>0:
                s+=n%10
                n//=10
            return s
        totSum,eleSum = 0,0
        for i in nums:
            totSum += i
            eleSum += sumOfDigits(i)
        return totSum - eleSum if totSum > eleSum else eleSum - totSum