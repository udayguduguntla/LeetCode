class Solution:
    def search(self, n: List[int], t: int) -> int:
        if t not in n:
            return -1
        else:
            return n.index(t)