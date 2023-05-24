class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited=set()
        n=len(grid)
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        def valid(r,c):
            return r>=0 and c>=0 and r<n and c<n
        # 1. Add to visited
        # 2. Push onto the queue
        def dfs(r,c):        
            if not valid(r,c) or not grid[r][c] or (r,c) in visited:
                return
            visited.add((r,c))
            for x,y in dirs:
                dfs(r+x,c+y)
        
        def bfs(r,c):
            dq=deque(visited)
            res=0
            while dq:
                for _ in range(len(dq)):
                    r,c=dq.popleft()
                    for x,y in dirs:
                        rr,cc=r+x,c+y
                        if not valid(rr,cc) or (rr,cc) in visited:
                            continue
                        if grid[rr][cc]:
                            return res
                        visited.add((rr,cc))
                        dq.append((rr,cc))  
                res+=1
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs(r,c)
                    
                