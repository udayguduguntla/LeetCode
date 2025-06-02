class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        m=min(s,key=len)
        l=len(m)
        n=len(s)
        while l>0:
            c=0
            for i in s:
                if m==i[:l]:
                    c+=1
            if c==n:
                return m
            m=m[:-1]
            l-=1
        return ""