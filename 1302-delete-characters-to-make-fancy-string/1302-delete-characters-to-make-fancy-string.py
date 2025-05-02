class Solution:
    def makeFancyString(self, s: str) -> str:
        print(set(s))
        for i in set(s):
            a=i+i+i
            while a in s:
                s=s.replace(a,(i+i))
        return s