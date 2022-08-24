class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!='.':
                    temp=board[i][j]
                    if (i,temp) in sudoku or (temp,j) in sudoku or (temp,i//3,j//3) in sudoku:
                        return False
                    sudoku.add((i,temp))
                    sudoku.add((temp,j))
                    sudoku.add((temp,i//3,j//3))
        return True