class Solution:
    def climbStairs(self, n: int) -> int:
        # # dp array
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]
        
        # Fibonacci Number
        first = 1
        second = 1
        for i in range(2, n + 1):
            third = first + second
            first = second
            second = third
        return second
        