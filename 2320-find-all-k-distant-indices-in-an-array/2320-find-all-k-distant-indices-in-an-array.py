class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indices = [i for i, x in enumerate(nums) if x == key]
        res = set()
        for i in range(len(nums)):
            for j in indices:
                if abs(i-j) <= k:
                    res.add(i)
                    break
        return list(res)