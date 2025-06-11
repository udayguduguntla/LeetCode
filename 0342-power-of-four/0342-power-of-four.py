class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:  return False
        b=bin(n)[2:]
        return True if b.count('1') == 1 and b.count('0') & 1 ==0 else False