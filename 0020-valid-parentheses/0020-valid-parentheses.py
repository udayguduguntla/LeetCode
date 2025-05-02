class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        l=[]
        for i in s:
            if i in "({[":
                l.append(i)
            elif len(l)>0:
                if i == ")" and l[-1] != "(":
                    return False
                elif i == "}" and l[-1] != "{":
                    return False
                elif i == "]" and l[-1] != "[":
                    return False
                l.pop()
            else:
                return False
        if len(l) == 0:
            return True
        else:
            return False