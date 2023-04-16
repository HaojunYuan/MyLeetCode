class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Start from each gate, do DFS
        # Each gate is marked as 0. Also, the distance between the gate and itself is 0. 
        # We pass in a variable d=0 when we enter dfs.
        # For surrounding rooms, we can pass d+1 to the room.
        rows, cols=len(rooms),len(rooms[0])
        
        def dfs(r,c,d):
            if r<0 or c<0 or r==rows or c==cols or rooms[r][c]==-1:
                return
            if d>0 and rooms[r][c]<=d:
                return
            rooms[r][c]=d
            dfs(r-1,c,d+1)
            dfs(r+1,c,d+1)
            dfs(r,c+1,d+1)
            dfs(r,c-1,d+1)
            
        
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c]==0:
                    dfs(r,c,0)
        return rooms