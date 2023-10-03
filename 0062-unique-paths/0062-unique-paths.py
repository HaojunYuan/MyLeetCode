class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[1] * n for _ in range(m)]
        for r in range(1, m):
            for c in range(1, n):
                path[r][c] = path[r - 1][c] + path[r][c - 1]
        return path[-1][-1]