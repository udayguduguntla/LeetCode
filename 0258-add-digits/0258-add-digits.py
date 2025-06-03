class Solution:
    def addDigits(self, num: int) -> int:
        # while num>9:
        #     s=0
        #     while num>0:
        #         s+=num%10
        #         num//=10
        #     num=s
        # return num

        from functools import reduce
        while num>9:
            num=reduce( lambda x,y:x+y, list(map(int,str(num))) )
        return num