class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        c=0
        for i in range(len(tickets)):
            if i<=k:
                c+=min(tickets[k],tickets[i])
            else:
                c+=min(tickets[k]-1,tickets[i])
        return c
