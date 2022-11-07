class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[0]+[math.inf]*amount
        for i in range(amount+1):
            for c in coins:
                if i-c>=0:
                    dp[i]=min(dp[i],dp[i-c]+1)
        return dp[-1] if dp[-1]!=math.inf else -1