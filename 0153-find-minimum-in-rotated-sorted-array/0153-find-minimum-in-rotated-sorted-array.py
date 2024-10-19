class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]
        while l <= r:
            mid = l + (r - l) // 2
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1