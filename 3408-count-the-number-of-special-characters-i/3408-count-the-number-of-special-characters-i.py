class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        return sum(1 for i in set(word.lower()) if i in word and i.upper() in word)