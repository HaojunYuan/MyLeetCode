class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        n = len(nums)
        while i<n:
            # We sort the positive integres in the array, 1, 2, 3, ...
            # j is the index that nums[i] should be placed
            j = nums[i] - 1
            if 0<= j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
                