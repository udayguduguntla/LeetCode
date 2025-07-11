class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        h = "0123456789abcdef"
        res = ""
        if num < 0:
            num &= 0xFFFFFFFF
        while num > 0:
            res = h[num % 16] + res
            num //= 16
        return res