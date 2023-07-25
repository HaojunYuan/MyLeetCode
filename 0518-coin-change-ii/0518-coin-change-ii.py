class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # # dp is a 2d list
        # dp=[[0]*len(coins) for _ in range(amount+1)]
        # dp[0]=[1]*len(coins)
        # for i in range(1, amount+1):
        #     for j in range(len(coins)):
        #         dp[i][j]=dp[i][j-1]
        #         if i-coins[j]>=0:
        #             dp[i][j]+=dp[i-coins[j]][j]
        # return dp[amount][-1]
        
        # only use 1d array for dp
        dp=[0]*(amount+1)
        dp[0]=1
        for i in range(len(coins)):
            nextDP=[0]*(amount+1)
            nextDP[0]=1
            
            for j in range(1, amount+1):
                nextDP[j]=dp[j]
                if j-coins[i]>=0:
                    nextDP[j]+=nextDP[j-coins[i]]
            dp=nextDP
        return dp[amount]
        