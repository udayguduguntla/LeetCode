class Solution:
    def minSwaps(self, s: str) -> int:
        x=0
        for i in s:
            if i == '[':
                x+=1
            elif x>0:
                x-=1
        return (x+1)//2