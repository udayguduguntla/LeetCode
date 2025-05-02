class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        a=0
        l=list(filter(lambda i: s[i] == goal[0], range(len(s))))
        for i in l:
            if s[i:]+s[:i]==goal:
                return True
        return False