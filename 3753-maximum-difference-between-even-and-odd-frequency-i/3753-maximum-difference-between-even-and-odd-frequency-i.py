class Solution:
    def maxDifference(self, s: str) -> int:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        d=sorted(set(d.values()))
        a,b=max(filter(lambda i:i & 1 == 1,d)),min(filter(lambda i:i & 1 == 0,d))
        return a-b