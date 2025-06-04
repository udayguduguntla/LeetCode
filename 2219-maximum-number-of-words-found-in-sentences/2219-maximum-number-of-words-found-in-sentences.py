class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        for i in range(len(sentences)):
            sentences[i] = sentences[i].split()
        return len(max(sentences,key=len))