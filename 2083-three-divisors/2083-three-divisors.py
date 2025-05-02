class Solution:
    def isThree(self, n: int) -> bool:
        c=1
        c+=len([i for i in range(1,(n//2)+1) if n%i==0])
        if c==3:
            return True
        else:
            return False