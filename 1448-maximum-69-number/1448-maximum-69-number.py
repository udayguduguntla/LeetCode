class Solution:
    def maximum69Number (self, num: int) -> int:
        s=list(str(num))
        if '6' not in s: return num
        return num + (10 ** (len(s) - s.index('6') - 1)) * 3