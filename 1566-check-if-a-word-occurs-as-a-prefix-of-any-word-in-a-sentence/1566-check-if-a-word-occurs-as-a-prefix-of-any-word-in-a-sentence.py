class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        c=0
        for i in sentence.split():
            c=c+1
            if i.startswith(searchWord):
                return c
        return -1