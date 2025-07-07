class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        res = []
        n = len(nums)
        for i in range(1 << n):
            sub = []
            for j in range(n):
                if (i >> j) & 1:
                    sub.append(nums[j])
            sub = tuple(sub)
            if sub not in seen:
                seen.add(sub)
                res.append(sub)
        return res