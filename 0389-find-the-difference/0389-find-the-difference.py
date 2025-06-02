class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sv=sum(map(ord,s))
        tv=sum(map(ord,t))
        return chr(tv-sv)