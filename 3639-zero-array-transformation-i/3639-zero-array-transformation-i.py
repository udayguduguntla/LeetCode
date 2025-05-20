class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        ops = [0] * (n + 1)

        for l, r in queries:
            ops[l] += 1
            if r + 1 < n:
                ops[r + 1] -= 1

        curr = 0
        for i in range(n):
            curr += ops[i]
            if curr < nums[i]:
                return False

        return True
