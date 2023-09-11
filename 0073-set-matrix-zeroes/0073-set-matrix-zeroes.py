class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        # Find rows and columns with zeros
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Set rows to zero
        for row in zero_rows:
            for j in range(cols):
                matrix[row][j] = 0

        # Set columns to zero
        for col in zero_cols:
            for i in range(rows):
                matrix[i][col] = 0
        