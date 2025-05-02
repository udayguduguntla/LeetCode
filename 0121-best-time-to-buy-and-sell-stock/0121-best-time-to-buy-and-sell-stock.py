class Solution:
    def maxProfit(self, p: List[int]) -> int:
        one=p[0]
        gain=0
        for i in range(1,len(p)):
            gain = max(gain,p[i]-one)
            one = min(one,p[i])
        return gain