class Solution:
    def firstUniqChar(self, s: str) -> int:
        st=list(set(s));m=len(s);i=0;f=0
        while i<len(st):
            if s.count(st[i])==1 and s.index(st[i])<m:
                m=s.index(st[i]);f=1
            i+=1
        return m if f==1 else -1