class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp is a 2d list
        dp=[[0]*len(coins) for _ in range(amount+1)]
        dp[0]=[1]*len(coins)
        for i in range(1, amount+1):
            for j in range(len(coins)):
                dp[i][j]=dp[i][j-1]
                if i-coins[j]>=0:
                    dp[i][j]+=dp[i-coins[j]][j]
        return dp[amount][-1]
        