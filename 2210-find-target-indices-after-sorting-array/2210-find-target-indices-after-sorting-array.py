class Solution:
    def binary_search_left(self,nums, target):
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            return low
        
    def binary_search_right(self,nums, target):
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return low
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = self.binary_search_left(nums, target)
        right = self.binary_search_right(nums, target)
        return list(range(left,right))