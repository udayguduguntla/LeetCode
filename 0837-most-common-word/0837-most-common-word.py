class Solution:
    def mostCommonWord(self, p: str, b: List[str]) -> str:
        p=p.lower();l=[".",",","!","?",";","\'","\""]
        for i in l:
            if i  in p:
                p=p.replace(i," ")
        p=p.split();p1=list(set(p))
        c,c1=0,''
        for i in p1:
            if (i not in b) and (p.count(i)>c):
                c1=i;c=p.count(i)
        return c1