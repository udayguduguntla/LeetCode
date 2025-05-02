class Solution:
    def rom(self, c):
        match c:
            case 'I':   return 1
            case 'V':   return 5
            case 'X':   return 10
            case 'L':   return 50
            case 'C':   return 100
            case 'D':   return 500
            case 'M':   return 1000
    def romanToInt(self, s: str) -> int:
        s=list(s)
        su=0;c=self.rom(s[0])
        for i in range(1,len(s)):
            n=self.rom(s[i])
            if c<n:   su-=c
            else:   su+=c
            c=n
        return su+c