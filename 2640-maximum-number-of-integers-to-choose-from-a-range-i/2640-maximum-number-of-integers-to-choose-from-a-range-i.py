class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        b = set(banned)
        i, s, count = 1, 0, 0
        while i <= n:
            if i not in b:
                s += i
                count += 1
            if s > maxSum:
                break
            i += 1
        if s <= maxSum:
            return count
        if s > maxSum:
            return count - 1