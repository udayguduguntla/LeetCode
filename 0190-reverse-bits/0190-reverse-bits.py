class Solution:
    def reverseBits(self, n: int) -> int:
        num = 0
        for _ in range(32):
            num = (num << 1) | n & 1
            n >>= 1
        return num