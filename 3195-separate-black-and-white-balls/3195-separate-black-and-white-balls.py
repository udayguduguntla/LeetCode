class Solution:
    def minimumSteps(self, s: str) -> int:
        c,d,f=0,0,0
        for i in range(len(s)):
            if f==0:
                if s[i]=='1':
                    f=1
                else:
                    d+=1
            else:
                if s[i]=='0':
                    c+=(i-d);d+=1
        return c