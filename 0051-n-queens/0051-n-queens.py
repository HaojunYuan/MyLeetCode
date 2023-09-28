class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        board = [['.'] * n for _ in range(n)]
        self.solve(0, board, n)
        return self.res
    
    def solve(self, r, board, n):
        if r == n:
            self.res.append([''.join(row) for row in board])
            return
        # else we try to place a queen on each column and backrack
        for c in range(n):
            if self.isValid(board, r, c):
                board[r][c] = 'Q'
                self.solve(r + 1, board, n)
                board[r][c] = '.'
    def isValid(self, board, row, col):
        # check all previous rolls
        for r in range(row):
            if board[r][col] == 'Q' or abs(row - r) == abs(col - board[r].index('Q')):
                return False
        return True