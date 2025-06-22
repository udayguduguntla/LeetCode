class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        i,l,n=0,[],len(s)
        while i < n:
            l.append(s[i:min(i+k,n)])
            i += k
        if len(l[-1]) < k:
            l[-1] += fill*(k-len(l[-1]))
        return l