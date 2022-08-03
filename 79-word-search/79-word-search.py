class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False
        row,col,w=len(board),len(board[0]),len(word)-1
        
        def dfs(i,j,k):
            if i<0 or j<0 or i>=row or j>=col:
                return False
            if board[i][j]=='#':
                return False
            if board[i][j]!=word[k]:
                return False
            if k==w:
                return True
            
            temp=board[i][j]
            board[i][j]='#'
            
            k+=1
            
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if dfs(x,y,k):
                    return True
            
            board[i][j]=temp
            return False
        
        for i in range(row):
            for j in range(col):
                if dfs(i,j,0):
                    return True
        
        return False