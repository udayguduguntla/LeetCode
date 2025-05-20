class Solution:
    def singlesum(self,s):
        s=int(s)
        tot=0
        while s > 0:
            tot += s % 10
            s //= 10
        return str(tot)
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s="".join(self.singlesum(s[i : min(i+k, len(s))]) for i in range(0,len(s),k))
        return s