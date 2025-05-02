class Solution:
    def isPalindrome(self, n: int) -> bool:
        n=list(str(n))
        if n==n[::-1]:
            return 1
        else:   return 0