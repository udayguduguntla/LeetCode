class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not set(s).issubset(set(t)):
            return False
        # for i in range(len(s)):
        #     if s[i] in t:
        #         t=t[t.index(s[i])+1:]
        #     else:
        #         return False
        # return True

        # approach - 2

        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)