class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        row=len(grid)
        col=len(grid[0])
        
        rotten=deque()
        fresh=0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    rotten.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        
        time=0
        while rotten and fresh>0:
            time+=1
            for _ in range(len(rotten)):
                r,c=rotten.popleft()
                for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                    rr,cc=r+x,c+y
                    if rr<0 or cc<0 or rr>=row or cc>=col or grid[rr][cc]!=1:
                        continue
                    grid[rr][cc]=2
                    rotten.append((rr,cc))
                    fresh-=1
        return time if fresh==0 else -1