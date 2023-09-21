class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # get all permutations and compare
        for i in range(len(nums) - 1, -1, -1):
            if i > 0 and nums[i] > nums[i - 1]:
                # swap the two indices
                # sort nums[i + 1:]
                for j in range(len(nums) -1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        nums[i:] = sorted(nums[i:])
                        return
        else:
            nums.sort()  # Reverse the list in-place
            return
