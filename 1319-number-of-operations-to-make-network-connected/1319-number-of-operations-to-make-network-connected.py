class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1: return -1
        
        mapp=[set() for i in range(n)]
        for i,j in connections:
            mapp[i].add(j)
            mapp[j].add(i)
        
        
        visited=[0]*n
        def dfs(i):
            if visited[i]: return 0
            visited[i]=1
            for j in mapp[i]:
                dfs(j)
            return 1
        
        return sum(dfs(i) for i in range(n))-1