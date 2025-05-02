class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s=sorted(list(s1));l=len(s)
        for i in range(len(s2)-l+1):
            a=sorted(list(s2[i:i+l]))
            if a == s:
                return True
        return False