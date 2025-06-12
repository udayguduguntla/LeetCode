class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a,b,c,newWords=set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm"),[]
        for word in words:
            ch = set(word.lower())
            if ch.issubset(a) or ch.issubset(b) or ch.issubset(c): newWords.append(word)
        return newWords