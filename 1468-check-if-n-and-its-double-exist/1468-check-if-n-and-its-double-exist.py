class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr)):
            a=2*arr[i]
            if a in arr and arr.index(a) != i:
                return True
        return False
        