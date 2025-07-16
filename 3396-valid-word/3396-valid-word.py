class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        d, v, c = 0, 0, 0
        for i in word:
            if i.isalnum():
                if i.isalpha():
                    if i in set("aeiouAEIOU"):
                        v += 1
                    else:
                        c += 1
                d += i.isdigit()
            else:
                return False
        if v >= 1 and c >= 1:
            return True
        return False