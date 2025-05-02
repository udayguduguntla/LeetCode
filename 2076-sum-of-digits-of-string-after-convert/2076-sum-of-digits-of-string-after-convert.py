class Solution:
    def getLucky(self, s: str, k: int) -> int:
        a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        n=""
        for i in s:
            n+=str(a.index(i)+1)
        while k>0:
            n=sum([int(f) for f in str(n)])
            k-=1
        return n