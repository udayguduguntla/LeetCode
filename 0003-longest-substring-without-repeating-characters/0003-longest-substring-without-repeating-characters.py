class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=0;l=len(s);i=0;j=0;s1=set()
        while i<l:
            while s[i] in s1 and i>=j:
                s1.remove(s[j])
                j+=1
            s1.add(s[i])
            m=max(m,len(s1))
            i+=1
        return m