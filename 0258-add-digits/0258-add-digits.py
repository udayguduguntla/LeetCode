class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            temp=num
            s=0
            while temp > 0:
                s+=temp%10
                temp //= 10
            num=s
        return num