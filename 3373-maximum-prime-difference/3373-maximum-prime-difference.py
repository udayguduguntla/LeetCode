class Solution:
    def isPrime(self, n: int) -> bool:
        if n in [2,3]: return True
        if n & 1 == 0 or n < 2: return False
        for i in range(3,int(n ** (0.5))+1, 2):
            if n % i == 0: return False
        return True
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            if self.isPrime(nums[i]) and self.isPrime(nums[j]): 
                return j - i
            if not self.isPrime(nums[i]):
                i += 1
            if not self.isPrime(nums[j]):
                j -= 1
        return 0