class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indices = [i for i, x in enumerate(nums) if x == key]
        res = set()
        for i in range(len(nums)):
            if i not in res:
                for j in indices:
                    if abs(i-j) <= k:
                        res.add(i)
        return list(res)