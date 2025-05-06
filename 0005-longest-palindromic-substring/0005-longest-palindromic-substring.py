class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) in [0,1]:
            return s
        if s==s[::-1]:
            return s
        left,right=0,len(s)
        res=""
        while left<right:
            temp=right
            while temp>left:
                subst=s[left:temp]
                if subst == subst[::-1] and len(res)<len(subst) :
                    res=subst
                temp-=1
            temp=left
            while temp<right:
                subst=s[temp:right]
                if subst == subst[::-1] and len(res)<len(subst) :
                    res=subst
                temp+=1
            left+=1
            right-=1
        return res