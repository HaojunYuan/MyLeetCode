class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        k = 1
        for j in range(1, len(nums)):
            if i + 1 < len(nums) and nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                k += 1
        return k
                