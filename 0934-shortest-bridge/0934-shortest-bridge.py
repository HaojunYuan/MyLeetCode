class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited=set()
        n=len(grid)
        # 1. Add to visited
        # 2. Push onto the queue
        def dfs(r,c):        
            if r<0 or c<0 or r==n or c==n or not grid[r][c] or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    dfs(r,c)     
                    dq=deque(visited)
                    res=0
                    while dq:
                        for _ in range(len(dq)):
                            r,c=dq.popleft()
                            for x,y in ([r+1,c],[r-1,c],[r,c-1],[r,c+1]):
                                if 0<=x<n and 0<=y<n and (x,y) not in visited:
                                    if grid[x][y]:
                                        return res
                                    visited.add((x,y))
                                    dq.append((x,y))  
                        res+=1
                