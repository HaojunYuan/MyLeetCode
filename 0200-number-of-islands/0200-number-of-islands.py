class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.bfs(grid,i,j)
                    res+=1
        return res
    
    def bfs(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1':
            return
        grid[i][j]='0'
        self.bfs(grid,i+1,j)
        self.bfs(grid,i-1,j)
        self.bfs(grid,i,j+1)
        self.bfs(grid,i,j-1)                