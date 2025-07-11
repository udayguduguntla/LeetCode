class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        is_prime = [True] * (32 + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(32 ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, 32 + 1, i):
                    is_prime[j] = False
        count = 0
        for n in range(left, right + 1):
            c,num = 0,n
            while num > 0:
                if num & 1:
                    c += 1
                num >>= 1
            count += is_prime[c]
        return count