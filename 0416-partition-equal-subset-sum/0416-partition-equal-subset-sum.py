class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2!=0:
            return False
        
        subsum=s//2
        dp=[0]*(subsum+1)
        dp[0]=1
        for num in nums:
            for j in range(subsum,num-1,-1):
                dp[j]=dp[j] or dp[j-num]
        
        return dp[subsum]