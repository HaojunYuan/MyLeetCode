class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Every time we meet a number, we need to know if there is any duplicates in its row, column and 3*3 sub box
        # Initialize a set to store the information
        # If there is any duplicates, return false
        # If we finish the sudoku and do not find any duplicates, return true
        rows=set()
        cols=set()
        blocks=set()
        for r in range(9):
            for c in range(9):
                if board[r][c]!='.':
                    number=board[r][c]
                    # If there is duplicates, return false
                    if (number,r) in rows or (number,c) in cols or (number,r//3,c//3) in blocks:
                        return False
                    # Add the new number to all sets
                    rows.add((number,r))
                    cols.add((number,c))
                    blocks.add((number,r//3,c//3))
        return True