class Solution:
    def isPalindrome(self, st: str) -> bool:
        s=""
        for i in st:
            if i.isalnum():
                s+=i
        s="".join(s.lower())
        if s == s[::-1]:
            return True
        else:
            return False