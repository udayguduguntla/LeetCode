class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[[1]]
        for i in range(2,numRows+1):
            l.append([1] + [0]*(i-2) + [1])
        for i in range(2,numRows):
            for j in range(1,i):
                l[i][j] += l[i-1][j-1]+l[i-1][j]
        return l