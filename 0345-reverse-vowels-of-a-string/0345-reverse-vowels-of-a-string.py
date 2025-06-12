class Solution:
    def reverseVowels(self, s: str) -> str:
        s,i,j,v=list(s),0,len(s)-1,set('aeiouAEIOU')
        while i<j:
            while s[i] not in v and i<j: i+=1
            while s[j] not in v and i<j: j-=1
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return "".join(s)