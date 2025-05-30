class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],[])+[i]
        for i in d.values():
            for j in range(len(i)-1):
                if  abs(i[j] -i[j+1]) <= k:
                    return True
        return False