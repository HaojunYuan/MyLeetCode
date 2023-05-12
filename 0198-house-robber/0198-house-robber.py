class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3: return max(nums)
        rob1,rob2=0,0
        dp=[0]*len(nums)
        for i in range(len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]