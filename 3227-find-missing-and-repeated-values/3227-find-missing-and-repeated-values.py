class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l=[]
        for i in grid:
            l+=i
        from collections import Counter
        for i,j in Counter(l).items():
            if j==2:
                return [i, min(set(range(1,len(grid)**2+1)) - set(l))]