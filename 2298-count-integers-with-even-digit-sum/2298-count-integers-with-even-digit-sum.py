class Solution:
    def digitsum(self, n):
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s
    def countEven(self, num: int) -> int:
        return sum(1 for i in range(1,num+1) if self.digitsum(i)%2==0)
        