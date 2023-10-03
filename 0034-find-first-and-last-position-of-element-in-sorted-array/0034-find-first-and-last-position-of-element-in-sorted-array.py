class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search
        # 1st search: find left boundary
        # 2nd search: find right boundary
        left = self.searchLeft(nums, target)
        right = self.searchRight(nums, target)
        if 0 <= left < len(nums) and 0 <= right < len(nums) and left <= right and nums[left] == target:
            return [left, right]
        else:
            return [-1, -1]
    
    def searchLeft(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l
    
    def searchRight(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return r
                