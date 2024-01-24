class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            # any positive nums[i] should be placed on nums[i] - 1: [1, 2, 3 ... ]
            target = nums[i] - 1
            if 0 <= target < len(nums) and nums[target] != nums[i]:
                nums[target], nums[i] = nums[i], nums[target]
            else:
                # move on
                i += 1
        for i, n in enumerate(nums):
            if i + 1 != n:
                return i + 1
        return len(nums) + 1