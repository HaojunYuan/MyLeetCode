class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid,i,j):
            if i<0 or j<0 or i>=r or j>=c or grid[i][j]!=1:
                return 0
            grid[i][j]=0
            return 1+dfs(grid,i+1,j)+dfs(grid,i-1,j)+dfs(grid,i,j+1)+dfs(grid,i,j-1)
        
        
        r=len(grid)
        c=len(grid[0])
        res=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    area=dfs(grid,i,j)
                    res=max(res,area)
        return res