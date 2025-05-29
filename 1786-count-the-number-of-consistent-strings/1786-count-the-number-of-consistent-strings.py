class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        for i in words:
            for j in i:
                if j not in list(allowed):
                    break
            else:
                c+=1
        return c