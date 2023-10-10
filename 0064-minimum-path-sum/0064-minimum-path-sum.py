class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[math.inf for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[-1][-1] = grid[-1][-1]
        for i in range(len(grid) - 2, -1, -1):
            dp[i][-1] = grid[i][-1] + dp[i + 1][-1]
        for j in range(len(grid[0]) - 2, -1, -1):
            dp[-1][j] = grid[-1][j] + dp[-1][j + 1]
        for i in range(len(grid) - 2, -1, -1):
            for j in range(len(grid[0]) - 2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]
#         return self.process(grid, 0, 0)
    
#     def process(self, grid, row, col):
#         if row == len(grid) - 1 and col == len(grid[0]) - 1:
#             return grid[row][col]
#         # go right
#         curr = grid[row][col]
#         if row == len(grid) - 1:
#             return curr + self.process(grid, row, col + 1)
#         elif col == len(grid[0]) - 1:
#             return curr + self.process(grid, row + 1, col)
#         else:
#             p1 = self.process(grid, row, col + 1)
#             p2 = self.process(grid, row + 1, col)
#             return curr + min(p1, p2)