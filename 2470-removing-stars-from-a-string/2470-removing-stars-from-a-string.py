class Solution:
    def removeStars(self, s: str) -> str:
        l=[]
        for i in range(len(s)):
            if s[i] == '*' and len(l)!=0:
                l.pop()
                continue
            l.append(s[i])
        return "".join(l)