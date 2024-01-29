class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set = set()
        col_set = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    row_set.add(r)
                    col_set.add(c)
        
        for r in row_set:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0
        
        for r in range(len(matrix)):
            for c in col_set:
                matrix[r][c] = 0