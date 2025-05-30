class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        tot_wealth=[sum(i) for i in accounts]
        return max(tot_wealth)