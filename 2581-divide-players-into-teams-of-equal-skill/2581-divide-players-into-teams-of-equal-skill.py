class Solution:
    def dividePlayers(self, s: List[int]) -> int:
        s=sorted(s);i=0;j=len(s)-1;su=s[i]+s[j];t=0
        if sum(s)%(len(s)//2) != 0: return -1 
        while i<j:
            if s[i]+s[j] == su:
                t+= s[i]*s[j]
            else:
                return -1
            i+=1;j-=1
        return t