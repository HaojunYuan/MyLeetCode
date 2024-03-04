class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if nums[i + 1] < nums[i], then nums[i + 1] is the minimum
        # we need to find such pattern using binary search
        
        l = 0
        r = len(nums) - 1
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