class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return (sum(nums) - sum(int(i) for i in "".join(list(map(str,nums)))))