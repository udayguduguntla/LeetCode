class Solution:
    def isPrime(self, n: int) -> bool:
        if n < 2:
            return False
        if n in {2, 3}:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]

    def primePalindrome(self, n: int) -> int:
        if 8 <= n <= 11:
            return 11
        for length in range(1, 6):  # only up to 10^8 needed
            for root in range(10 ** (length - 1), 10 ** length):
                s = str(root)
                p = int(s + s[-2::-1])  # Generate odd-length palindrome
                if p >= n and self.isPrime(p):
                    return p