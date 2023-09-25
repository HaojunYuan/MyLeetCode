class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        dp = [[1] for _ in range(numRows)]
        dp[1] = [1, 1]
        for i in range(2, numRows):
            for j in range(len(dp[i - 1]) - 1):
                dp[i].append(dp[i - 1][j] + dp[i - 1][j + 1])
            dp[i].append(1)
        return dp
                    
            