class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def helper(grid,i,j):
            if i<0 or j<0 or i>=row or j>=col or grid[i][j]!=1:
                return 0
            grid[i][j]=0
            
            return 1+helper(grid,i+1,j)+helper(grid,i-1,j)+helper(grid,i,j+1)+helper(grid,i,j-1)
            
            
        row=len(grid)
        col=len(grid[0])
        res=0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    area=helper(grid,i,j)
                    res=max(res,area)
        
        return res