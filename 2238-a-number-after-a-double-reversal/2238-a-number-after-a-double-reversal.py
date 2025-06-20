class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # return num == int(str(int(str(num)[::-1]))[::-1])

        def revNum(n):
            s = 0
            while n > 0:
                s = s * 10 + n % 10
                n //= 10
            return s
        return num == revNum(revNum(num))