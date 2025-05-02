class Solution:
    def convert(self, s: str, n: int) -> str:
        if len(s)==1 or len(s)==2 or n==1:
            return s
        l=[s[0]]+[""]*(n-1);le=len(s);i=0
        while i<le:
            j=1
            while (j<n) and i<le:
                i+=1
                if i>le-1:
                    return "".join(l)
                l[j]+=s[i];j+=1
            j=n-2
            while (j>-1):
                i+=1
                if i>le-1:
                    return "".join(l)
                l[j]+=s[i];j-=1
        return "".join(l)