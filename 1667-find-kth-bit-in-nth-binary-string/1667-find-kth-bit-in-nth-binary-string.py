class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s=['0']
        for i in range(1,n):
            a=s[-1].replace('1', '2').replace('0', '1').replace('2', '0')
            s.append(s[-1]+"1"+a[::-1]);del s[0]
        return s[-1][k-1]