class Solution:
    def minimumSum(self, num: int) -> int:
        n=sorted([int(i) for i in str(num)])
        return n[0]*10 + n[-1] + n[1]*10 + n[-2]