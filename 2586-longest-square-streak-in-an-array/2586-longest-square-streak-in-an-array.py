class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums=set(nums);m=-1
        for i in sorted(list(nums)):
            if i not in nums:   continue
            c=1;u=i
            print(i,c)
            while u*u in nums:
                c+=1;u=u*u;nums.remove(u)
            m= max(m,c) if c>1 else m
        return m