class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(set(pattern)) != len(set(s)) or len(pattern) != len(s):  return False
        d = {}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = s[i]
            elif d[pattern[i]] != s[i]:
                return False
        return True