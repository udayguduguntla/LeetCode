class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                p, q = j + 1, n - 1
                while p < q:
                    s = nums[i] + nums[j] + nums[p] + nums[q]
                    if s == target:
                        result.add((nums[i], nums[j], nums[p], nums[q]))
                        p += 1
                        q -= 1
                    elif s < target:
                        p += 1
                    else:
                        q -= 1

        return [list(quad) for quad in result]
