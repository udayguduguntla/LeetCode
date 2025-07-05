class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        freq = sorted(freq,key=lambda i:freq[i],reverse = True)
        return freq[:k]