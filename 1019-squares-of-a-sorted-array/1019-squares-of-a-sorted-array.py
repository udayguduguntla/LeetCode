class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # nums=[i**2 for i in nums]
        return sorted(map(lambda x:x**2,nums))