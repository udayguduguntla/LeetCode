class Solution:
    def maxDistance(self, c: List[int]) -> int:
        m=0
        for i in range(len(c)-1):
            for j in range(i,len(c)):
                if (c[i] != c[j]) and m<abs(i-j):
                    m=abs(i-j)
        return m