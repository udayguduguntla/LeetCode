class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(math.isqrt(c))
        while i <= j:
            val = i**2 + j**2
            if val == c:
                return True
            if val > c:
                j -= 1
            else:
                i += 1
        return False