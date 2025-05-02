class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=len(h);m,i,j=0,0,l-1
        while i<j:
            m=max(m, abs(i-j)*min(h[i],h[j]))
            if h[i]>h[j]: j-=1
            elif h[i]<h[j]: i+=1
            else:
                if h[i+1]>h[j-1]:   i+=1
                else:   j-=1
        return m