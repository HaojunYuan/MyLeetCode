class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return -1
        row=len(grid)
        col=len(grid[0])
        
        #queue for bfs with rotten orange
        rotten=deque()
        
        #count of fresh orange
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
                x,y=rotten.popleft()
                for x1,y1 in [(1,0),(-1,0),(0,1),(0,-1)]:
                    xx,yy=x+x1,y+y1
                    if xx<0 or yy<0 or xx>=row or yy>=col or grid[xx][yy]==2 or grid[xx][yy]==0:
                        continue
                    grid[xx][yy]=2
                    rotten.append((xx,yy))
                    fresh-=1
                
        return time if fresh==0 else -1