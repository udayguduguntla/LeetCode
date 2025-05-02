class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        s1 = ""
        if s == "": return 0
        l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        f = -1 if s[0] == '-' else 1 if s[0] == '+' else 0
        u = 1 if f != 0 else 0
        if s[u:] == "": return 0
        for i in s[u:]:
            if i in l:  s1 += i
            elif not i.isnumeric():  break
        if s1 == "":    return 0
        s1 = f * int(s1) if u else int(s1)
        return max(-2**31, min(2**31 - 1, s1))