class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        m = float('inf')
        l = []
        for i in range(len(arr)-1):
            m1 = arr[i+1] - arr[i]
            if m1 < m:
                m = m1
                l = [[arr[i], arr[i+1]]]
            elif m1 == m:
                l.append([arr[i], arr[i+1]])
        return l