class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l=deque();x=0
        for i in s:
            if i=='(':
                l.append(1)
            else:
                if l:
                    l.pop()
                else:
                    x+=1
        return x+len(l)