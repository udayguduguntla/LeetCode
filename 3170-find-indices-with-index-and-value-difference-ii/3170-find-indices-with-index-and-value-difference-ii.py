class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        min_index = 0
        max_index = 0

        for i in range(indexDifference, n):
            if nums[i - indexDifference] < nums[min_index]:
                min_index = i - indexDifference
            if nums[i - indexDifference] > nums[max_index]:
                max_index = i - indexDifference

            if abs(nums[i] - nums[min_index]) >= valueDifference:
                return [i, min_index]
            if abs(nums[i] - nums[max_index]) >= valueDifference:
                return [i, max_index]

        return [-1, -1]
