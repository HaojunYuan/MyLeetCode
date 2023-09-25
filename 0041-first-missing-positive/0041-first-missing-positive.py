class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # we do not care about negative numbers and 0
        # if correctly ordered, nums[i] == i + 1
        # while nums[i] != i, swap nums[i] with nums[nums[i]]
        # place all numbers on the correct index. Iterate through the nums. If there isi a mis match, return the missing positive
        # otherwise, return len(nums) + 1
        i = 0
        while i < len(nums):
            targetIndex = nums[i] - 1
            if 0 <= targetIndex < len(nums) and nums[i] != nums[targetIndex]:
                nums[i], nums[targetIndex] = nums[targetIndex], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
                
        