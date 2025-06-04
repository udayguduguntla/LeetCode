class Solution:
    def lenOfSentences(self,s):
        return len(s.split())
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(map(self.lenOfSentences, sentences))