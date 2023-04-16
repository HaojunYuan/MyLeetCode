class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Edge "O" will not be captured
        # Iterate through the edge to see if there is any O
        # DFS each 'O' on the edge and mark them as 'a'
        # Iterate through the board and mark all 'O' as 'X'
        # Iterate through the board, return all 'a' back to 'O'
        rows,cols=len(board),len(board[0])
        
        def dfs(r,c):
            if r<0 or c<0 or r==rows or c==cols or board[r][c]!='O':
                return
            board[r][c]='a'
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        for r in range(rows):
            for c in range(cols):
                if r in (0,rows-1) or c in (0,cols-1):
                    dfs(r, c)
                    
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='X'
                    
                    
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='a':
                    board[r][c]='O'
        return board
        