class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if max(nums)>=len(nums):
            for i in range(len(nums)):
                if i not in nums:
                    return i
        else:
            return len(nums)