class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        from functools import reduce
        for i in range(len(accounts)):
            accounts[i] = reduce(lambda x,y : x+y, accounts[i])
        return max(accounts)