class Solution:
    def finalString(self, s: str) -> str:
        l=""
        for i in s:
            if i == "i":
                l=l[::-1]
            else:
                l += i
        return l