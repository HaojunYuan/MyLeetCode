class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r,c=len(matrix),len(matrix[0])
        i,j=0,-1
        direction=1
        res=[]
        while r*c>0:
            for _ in range(c):
                j+=direction
                res.append(matrix[i][j])
            r-=1
            for _ in range(r):
                i+=direction
                res.append(matrix[i][j])
            c-=1
            direction*=-1
        
        return res