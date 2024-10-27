class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # board
        self.res = []
        board = [['.'] * n for _ in range(n)]
        self.solve(0, board, n)
        return self.res
        
    def solve(self, row, board, n):
        # base case
        if row == n:
            self.res.append([''.join(row) for row in board])
            return
        for col in range(n):
            if self.isValid(row, col, board):
                board[row][col] = 'Q'
                self.solve(row + 1, board, n)
                board[row][col] = '.'
                
    def isValid(self, row, col, board):
        # check queens in previous rows
        for r in range(row):
            if board[r][col] == 'Q' or r - board[r].index('Q') == row - col or r + board[r].index('Q') == row + col:
                return False
        return True
            