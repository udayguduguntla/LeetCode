class Solution:
    def searchInsert(self, n: List[int], t: int) -> int:
        l,r=0,len(n)
        while l<r:
            m=(l+r)//2
            if t>n[m]:
                l=m+1
            else:
                r=m
        return l