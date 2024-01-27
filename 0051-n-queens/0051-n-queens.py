class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # create board
        self.res = []
        board = [['.'] * n for _ in range(n)]
        self.solve(0, board, n)
        return self.res
    
    def solve(self, row, board, n):
        # for every col of this row, try to put a queen there
        # base case
        if row == n:
            self.res.append([''.join(row) for row in board])
            return
        for col in range(n):
            if self.isValid(board, row, col):
                board[row][col] = 'Q'
                self.solve(row + 1, board, n)
                board[row][col] = '.'
                
    
    def isValid(self, board, row, col):
        # row, col and diagonals
        for r in range(row):
            if board[r][col] == 'Q' or r - board[r].index('Q') == row - col or r + board[r].index('Q') == row + col:
                return False
        return True