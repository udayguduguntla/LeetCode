class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        factors = set()
        n = min(a,b)
        for i in range(1, int(n**0.5) + 1):
            if a % i == 0 and b % i == 0:
                factors.add(i)
            j = n // i
            if a % j == 0 and b % j == 0:
                factors.add(j)
        return len(factors)