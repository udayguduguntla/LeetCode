class Solution:
    def maximumSwap(self, num: int) -> int:
        n=list(str(num));l=[0]*(len(n))
        n1=sorted(n,reverse=True)
        if n==n1:   return num
        max_idx = len(n) - 1
        for i in range(len(n) - 1, -1, -1):
            if n[i] > n[max_idx]:   max_idx = i
            l[i] = max_idx
        print(l)
        for i in range(len(n)):
            if n[i]!=n[l[i]]:
                n[i], n[l[i]] = n[l[i]], n[i]
                return int("".join(n))
        return num