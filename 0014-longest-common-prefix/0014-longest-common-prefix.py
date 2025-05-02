class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        m=min(s,key=len);l=len(m)
        while l>0:
            if all(m in i[:l] for i in s):
                return m
            m=m[:-1];l-=1
        return ""