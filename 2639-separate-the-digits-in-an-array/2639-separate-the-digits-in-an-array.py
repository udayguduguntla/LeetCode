class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        nums="".join(map(str,nums))
        return list(map(int, nums))