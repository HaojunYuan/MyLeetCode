class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        # Diagonals start with (row, 0)
        for i in range(rows):
            self.sort(mat, i, 0)
        for j in range(1, cols):
            self.sort(mat, 0, j)
        return mat
    
    def sort(self, mat, row, col):
        # [row, col] is the start of the diagonal
        m, n = len(mat), len(mat[0])
        i, j = row, col
        arr=[]
        while i < m and j < n:
            arr.append(mat[i][j])
            i += 1
            j += 1
        # Move the pointers back to the start of the diagonal cuz we need to modify the original matrix
        arr.sort()
        i, j = row, col
        while i < m and j < n:
            mat[i][j] = arr.pop(0)
            i += 1
            j += 1