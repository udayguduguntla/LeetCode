class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # approach - 1
        # k = k % len(nums)
        # nums.reverse()
        # nums[:k] = reversed(nums[:k])
        # nums[k:] = reversed(nums[k:])

        # approach - 2
        k = k % len(nums)
        left, right = 0,len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        left, right = 0,k-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        left, right = k,len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1