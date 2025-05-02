class Solution:
    def subsets(self, n: List[int]) -> List[List[int]]:
        l=[[]]
        for i in n:
            l+=[j+[i] for j in l]
        print(l)
        return l