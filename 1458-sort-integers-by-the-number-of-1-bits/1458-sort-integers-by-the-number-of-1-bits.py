class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countSet(n):
            c = 0
            while n:
                c += (n & 1)
                n >>=1
            return c
        d = dict()
        for i in arr:
            c = countSet(i)
            d[c] = d.get(c,[]) + [i]
        l = []
        for i in sorted(d):
            l.extend(sorted(d[i]))
        return l