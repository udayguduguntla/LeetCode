class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum(i.count('*') for i in s.split('|')[::2])