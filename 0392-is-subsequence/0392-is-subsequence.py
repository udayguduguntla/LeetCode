class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not set(s).issubset(set(t)):
            return False
        for i in range(len(s)):
            # if s.count(s[i]) != t.count(s[i]):
            #     return False
            if s[i] in t:
                t=t[t.index(s[i])+1:]
            else:
                return False
        return True