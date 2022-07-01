class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(i,j):
            image[i][j]=newColor
            for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0<=x<row and 0<=y<col and image[x][y]==color:
                    dfs(x,y)
        color,row,col=image[sr][sc],len(image),len(image[0])
        if color!=newColor:
            dfs(sr,sc)
        return image
            