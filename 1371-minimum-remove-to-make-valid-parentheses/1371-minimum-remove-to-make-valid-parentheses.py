class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l=[];l1=[];s=list(s)
        for i in range(len(s)):
            if s[i]=="(":
                l.append(i)
            elif s[i]==")":
                if l:
                    l.pop()
                else:
                    l1.append(i)
        print(l,l1)
        l=sorted(l+l1,reverse=True)
        print(l)
        for i in l:
            del s[i]
        return "".join(s)