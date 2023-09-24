class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # tranpose
        # left-right flip
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(r, cols):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for r in range(rows):
            for c in range(cols // 2):
                matrix[r][c], matrix[r][cols - c - 1] = matrix[r][cols - c - 1], matrix[r][c]
                
        
        