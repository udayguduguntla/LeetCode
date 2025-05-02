class Solution:
    def countMaxOrSubsets(self, nums):
        m = 0;c=0
        for num in nums:    m |= num
        def subset_or(subset):
            re = 0
            for num in subset:
                re |= num
            return re
        l = [[]]
        for i in nums:
            n = []
            for j in l:
                n1 = j + [i]
                n.append(n1)
                if subset_or(n1) == m:
                    c += 1
            l += n
        return c