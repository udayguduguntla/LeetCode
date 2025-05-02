class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        t=[];le=len(n);n=sorted(n)
        for i in range(le-2):
            if i==0 or (i>0 and n[i] != n[i-1]):
                l=i+1;r=le-1
                while l<r:
                    if n[l]+n[r] == 0-n[i]:
                        t.append([n[i],n[l],n[r]])
                        while l<r and n[l]==n[l+1]: l+=1
                        while l<r and n[r]==n[r-1]: r-=1
                        l+=1;r-=1
                    elif n[l]+n[r] > 0-n[i]: r-=1
                    else:   l+=1
        return t