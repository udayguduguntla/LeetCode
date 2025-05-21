class Solution:
    def digitSum(self,n):
        s=0
        while n>0:
            s+=n%10
            n//=10
        return s
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1):
            s=str(i)
            if len(s)%2==0 and self.digitSum(int(s[:len(s)//2])) == self.digitSum(int(s[len(s)//2:])):  count+=1
        return count