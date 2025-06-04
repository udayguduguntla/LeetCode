class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # return "".join(word1) == "".join(word2)

        a,b="",""
        for i in word1:
            a+=i
        for i in word2:
            b+=i
        return a==b