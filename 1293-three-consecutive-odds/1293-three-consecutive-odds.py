class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            c=0
            for i in arr[i:i+3]:
                if i & 1 == 1:
                    c+=1
            if c==3:
                return True
        return False