class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # two searches: first and last index
        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)
        return [first, last]
    
    def findFirst(self, nums, target):
        res = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                res = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return res
    
    def findLast(self, nums, target):
        res = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                res = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return res