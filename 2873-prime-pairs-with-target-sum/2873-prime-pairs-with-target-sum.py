class Solution:
    def prime(self, n: int) -> List[bool]:
        n = n + 1
        prime = [True] * n
        prime[0] = prime[1] = False
        for i in range(2,int(n ** (0.5)) + 1):
            if prime[i]:
                for j in range(i*i,n,i):
                    prime[j] = False
        return [i for i, val in enumerate(prime) if val]
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime = self.prime(n)
        i, j = 0, len(prime) - 1
        l = []
        while i <= j:
            s = prime[i] + prime[j]
            if s == n:
                l.append([prime[i],prime[j]])
                i += 1
                j -= 1
            elif s < n:
                i += 1
            else:
                j -= 1
        return list(l)