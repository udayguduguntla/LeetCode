class Solution:
    def clearDigits(self, s: str) -> str:
        if s.isalpha():  return s
        l=[]
        for i in s:
            if i.isdigit() and l:
                l.pop()
            else:
                l.append(i)
        return "".join(l)