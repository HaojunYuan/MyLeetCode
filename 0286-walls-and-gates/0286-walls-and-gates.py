class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # starting from each gate, mark the rooms with its distance to nearest gates
        # we only update the distance if the new distance is smaller than the current distance of the room (to avoid duplication and infinite loop)
        rows,cols=len(rooms),len(rooms[0])
        def bfs(r,c,d):
            if r<0 or c<0 or r==rows or c==cols or rooms[r][c]==-1:
                return
            if d>0 and rooms[r][c]<=d:
                return
            rooms[r][c]=d
            bfs(r+1,c,d+1)
            bfs(r-1,c,d+1)
            bfs(r,c+1,d+1)
            bfs(r,c-1,d+1)
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c]==0:
                    bfs(r,c,0)
                             