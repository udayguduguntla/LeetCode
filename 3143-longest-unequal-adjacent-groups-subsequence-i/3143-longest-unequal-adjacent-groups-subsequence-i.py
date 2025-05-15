class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        flag=0
        res=[]
        for i in range(len(groups)):
            if groups[i] == flag:
                res.append(words[i])
                flag= 1-flag
        flag=1
        res1=[]
        for i in range(len(groups)):
            if groups[i] == flag:
                res1.append(words[i])
                flag= 1-flag
        return res if len(res)>len(res1) else res1