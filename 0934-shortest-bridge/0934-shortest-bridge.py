class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # if we find a land, do dfs to get all land
        # for each level, for all nodes inside that level, do bfs towards the other island
        # common functionds
        dirs=[[1,0],[-1,0],[0,1],[0,-1]]
        n=len(grid)
        # a set for visited nodes
        visited=set()
        def isValid(r,c):
            return r>=0 and c>=0 and r<n and c<n
        
        def dfs(r,c):
            if not isValid(r,c) or (r,c) in visited or not grid[r][c]:
                return
            visited.add((r,c))
            for x,y in dirs:
                dfs(r+x,c+y)
        
        def bfs():
            res=0
            q=deque(visited)
            # we add to visited and the deque
            while q:
                for _ in range(len(q)):
                    r,c=q.popleft()
                    for x,y in dirs:
                        newr,newc=r+x,c+y
                        if not isValid(newr,newc) or (newr,newc) in visited:
                            continue
                        if grid[newr][newc]:
                            return res
                        q.append((newr,newc))
                        visited.add((newr,newc))
                res+=1
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()
        
        
                        