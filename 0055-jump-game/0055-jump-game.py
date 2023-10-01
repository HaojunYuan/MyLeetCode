class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[len(nums) - 1] = 1
        target = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= target and dp[target]:
                dp[i] = 1
                target = i
        return dp[0]
        
    
    