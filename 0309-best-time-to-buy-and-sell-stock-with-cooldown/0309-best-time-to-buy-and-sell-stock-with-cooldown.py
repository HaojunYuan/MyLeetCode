class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        # key = (i, action) value = maxProfit at index i given action    
        
        # return the maximum profit for taking the action at given index
        def dfs(i, buying):
            if i>=len(prices):
                return 0
            if (i,buying) in dp:
                return dp[(i, buying)]
            
            cooldown=dfs(i+1, buying)
            if buying:
                buy=dfs(i+1, not buying) - prices[i]
                dp[(i,buying)] = max(buy, cooldown)
            else:
                sell=dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)
            