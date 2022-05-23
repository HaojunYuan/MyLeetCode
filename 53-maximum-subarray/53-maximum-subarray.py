class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=-math.inf
        tempmax=0
        for num in nums:
            tempmax+=num
            maxsum=max(maxsum,tempmax)
            tempmax=max(tempmax,0)
        return maxsum