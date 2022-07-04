class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color=image[sr][sc]
        def dfs(i,j):
            image[i][j]=newColor
            for (x,y) in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=x<len(image) and 0<=y<len(image[0]) and image[x][y]==color:
                    dfs(x,y)
        if color!=newColor:
            dfs(sr,sc)
        return image