class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!='.':
                    num=board[i][j]
                    if (i,num) in sudoku or (num,j) in sudoku or (num,i//3,j//3) in sudoku:
                        return False
                    sudoku.add((i,num))
                    sudoku.add((num,j))  
                    sudoku.add((num,i//3,j//3))  
        return True