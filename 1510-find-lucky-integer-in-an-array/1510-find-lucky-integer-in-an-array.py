class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = dict()
        for i in arr:
            count[i] = count.get(i,0) + 1
        count = {key: count[key] for key in sorted(count.keys(), reverse=True)}
        count = list(count.items())
        for i,j in count:
            if i == j:
                return i
        return -1