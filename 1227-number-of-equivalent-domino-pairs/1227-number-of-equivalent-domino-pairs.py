class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c={}
        r=0
        for i in dominoes:
            a,b=i
            key=(a,b) if a<b else (b,a)
            if key in c:
                r+=c[key]
                c[key]+=1
            else:
                c[key]=1
        return r