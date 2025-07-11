class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2: return 1
        first, second = 1, 2
        for i in range(3, n + 1):
            cur = first + second
            first = second
            second = cur
        return second