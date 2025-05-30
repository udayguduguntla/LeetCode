class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            d[i] = d.get(i, 0) + 1
        d=dict(sorted(d.items(), key=lambda i: i[1], reverse = True))
        res=""
        for i,j in d.items():
            res+=i*j
        return res