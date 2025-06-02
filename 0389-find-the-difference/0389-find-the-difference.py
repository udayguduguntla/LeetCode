class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # sv=sum(map(ord,s))
        # tv=sum(map(ord,t))
        # return chr(tv-sv)
        from functools import reduce
        return chr(reduce(lambda a,b:a^b,map(ord,s+t)))