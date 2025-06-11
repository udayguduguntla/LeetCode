class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return
        else:
            from math import trunc
            res = trunc(dividend/divisor)
            if res > 2**31-1:
                return 2**31-1
            elif res < -2**31:
                return -2**31
            else:
                return res