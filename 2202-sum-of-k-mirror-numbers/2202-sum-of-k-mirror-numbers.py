class Solution:
    def is_k_palindrome(self, num: int, k: int) -> bool:
        rev = 0
        n = num
        while n:
            rev = rev * k + (n % k)
            n //= k
        return rev == num

    def generate_palindromes(self, length: int):
        start = 10**((length - 1) // 2)
        end = 10**((length + 1) // 2)
        odd = (length % 2 == 1)
        palindromes = []
        for half in range(start, end):
            s = str(half)
            if odd:
                pal = int(s + s[-2::-1])
            else:
                pal = int(s + s[::-1])
            palindromes.append(pal)
        return palindromes

    def kMirror(self, k: int, n: int) -> int:
        total = 0
        count = 0
        length = 1

        while count < n:
            pals = self.generate_palindromes(length)
            for pal in pals:
                if self.is_k_palindrome(pal, k):
                    total += pal
                    count += 1
                    if count == n:
                        return total
            length += 1
