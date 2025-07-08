class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == '?':
                # Find a letter that is different from adjacent ones
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if (i > 0 and s[i - 1] == c) or (i < len(s) - 1 and s[i + 1] == c):
                        continue
                    s[i] = c
                    break
        return "".join(s)