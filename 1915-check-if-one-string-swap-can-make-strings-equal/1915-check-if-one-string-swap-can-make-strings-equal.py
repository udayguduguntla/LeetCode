class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # approach - 1
        
        # from collections import Counter
        # if Counter(s1)!=Counter(s2):  return False
        # if len(s1) != len(s2):  return False
        # n=len(s1)
        # i,j=0,len(s1)-1
        # c=0
        # while i<j:
        #     if s1[i]!=s2[i]:  c+=1
        #     if s1[j]!=s2[j]:  c+=1
        #     if c>2:  return False
        #     i+=1
        #     j-=1
        # if len(s1)%2==1 and s1[n//2] != s2[n//2]:
        #     c+=1
        # return True if c<=2 else False

        # approach - 2
        
        
        # if len(s1) != len(s2):  return False
        # indices = [i for i in range(len(s1)) if s1[i] != s2[i]]
        # if not indices:
        #     return True
        # if len(indices) != 2:
        #     return False
        # return s1[indices[0]] == s2[indices[1]] and s1[indices[1]] == s2[indices[0]]

        # approach - 3

        if len(s1) != len(s2):  return False
        i,j = 0,len(s1)-1
        s1,s2=list(s1),list(s2)
        while s1[i]==s2[i] and i<j: 
            i+=1
        while s1[j]==s2[j] and i<j: 
            j-=1
        s1[i],s1[j] = s1[j],s1[i]
        return s1 == s2