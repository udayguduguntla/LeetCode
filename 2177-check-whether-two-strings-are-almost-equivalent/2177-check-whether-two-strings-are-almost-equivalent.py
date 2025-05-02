class Solution:
    def checkAlmostEquivalent(self, w1: str, w2: str) -> bool:
        s=list(set(w1))
        for i in s:
            if abs(w1.count(i)-w2.count(i)) > 3:
                return False
        s=list(set(w2)-set(w1))
        for i in s:
            if abs(w1.count(i)-w2.count(i)) > 3:
                return False
        return True