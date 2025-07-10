class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        mx_i = 0x7FFFFFFF
        while b != 0:
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = (carry << 1) & mask
        return a if a <= mx_i else ~(a ^ mask)