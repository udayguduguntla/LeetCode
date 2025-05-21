class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c=len(matrix),len(matrix[0])
        il,jl=[],[]
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    il.append(i)
                    jl.append(j)
        for i in range(r):
            for j in range(c):
                if i in il or j in jl:
                    matrix[i][j]=0
        return matrix