class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum,tempSum=nums[0],0
        for num in nums:
            tempSum=max(num,tempSum+num)
            maxSum=max(maxSum,tempSum)
        return maxSum