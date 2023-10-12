class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]
        while l <= r:
            mid = l + (r - l) // 2
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] < nums[l]:
                r = mid - 1
            else:
                l = mid + 1