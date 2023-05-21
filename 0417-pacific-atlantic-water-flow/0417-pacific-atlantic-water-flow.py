class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # start bfs from both p ocean and a ocean
        # two sets: p and a
        # starting with height 0. If the current height is higher than the prev height, then water can flow from this grid to the ocean. Add this grid to the set
        # continue bfs with updated prev height
        # Iterate through one set. If the height is also in another set, add it to the results
        pset,aset=set(),set()
        rows,cols=len(heights),len(heights[0])
        def bfs(r,c,s,prev):
            if r<0 or c<0 or r==rows or c==cols or heights[r][c]<prev or (r,c) in s:
                return 
            s.add((r,c))
            curr=heights[r][c]
            bfs(r+1,c,s,curr)
            bfs(r-1,c,s,curr)   
            bfs(r,c+1,s,curr)
            bfs(r,c-1,s,curr)
        
        # first and last rows:
        for c in range(cols):
            bfs(0,c,pset,-1)
            bfs(rows-1,c,aset,-1)
        
        # first and last cols:
        for r in range(rows):
            bfs(r,0,pset,-1)
            bfs(r,cols-1,aset,-1)
        
        # check for same grids in both sets, thats our results
        res=[]
        for r,c in pset:
            if (r,c) in aset:
                res.append([r,c])
        return res
        
            
        