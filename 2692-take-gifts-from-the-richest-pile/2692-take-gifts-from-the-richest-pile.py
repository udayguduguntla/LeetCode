from math import floor,sqrt
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            ind=gifts.index(max(gifts))
            gifts[ind]=floor(sqrt(gifts[ind]))
        return sum(gifts)