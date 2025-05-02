class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l=[];le=len(words);w=words[0]
        words=[list(i) for i in words]
        for i in w:
            c=0
            for j in words:
                if i in j:
                    j.remove(i)
                    c+=1
                if c==le:
                    l.append(i)
        return l