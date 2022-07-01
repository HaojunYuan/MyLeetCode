class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        maxSum,tempSum=-math.inf,0
        for num in nums:
            tempSum=max(num,tempSum+num)
            maxSum=max(maxSum,tempSum)
        return maxSum