class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if Counter(s1)!=Counter(s2):  return False
        if len(s1) != len(s2):  return False
        n=len(s1)
        i,j=0,len(s1)-1
        c=0
        while i<j:
            # print(s1[i]!=s2[i], s1[i], s2[i], i, "i")
            # print(s1[j]!=s2[j], s1[j], s2[j], j, "j")
            if s1[i]!=s2[i]:  c+=1
            if s1[j]!=s2[j]:  c+=1
            if c>2:  return False
            i+=1
            j-=1
        if len(s1)%2==1 and s1[n//2] != s2[n//2]:
            c+=1
        return True if c<=2 else False