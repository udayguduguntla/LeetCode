class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        s=deque()
        for i in expression:
            if i==')':
                v=[]
                while s[-1]!='(':
                    v.append(s.pop())
                s.pop()
                o=s.pop()
                if o=="!":
                    s.append('f' if v[0]=='t' else 't')
                elif o=="&":
                    f=0
                    for i in v:
                        if i=='f':
                            s.append('f');f=1;break
                    if f!=1:
                        s.append('t')
                elif o=="|":
                    f=0
                    for i in v:
                        if i=='t':
                            s.append('t');f=1;break
                    if f!=1:
                        s.append('f')
            elif i!=",":
                s.append(i)
        return s[-1]=='t'