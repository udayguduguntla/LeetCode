class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def smallFreq(s):
            if not s:
                return 0
            for i in "abcdefghijklmnopqrstuvwxyz":
                if i in s:
                    return s.count(i)
        words = [smallFreq(i) for i in words]
        queries = [smallFreq(i) for i in queries]
        res = []
        for i in queries:
            c = 0
            for j in words:
                if i < j:
                    c += 1
            res.append(c)
        return res