class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        l=map(str,d);l=int("".join(l))
        l+=1;l=list(str(l))
        return map(int,l)
