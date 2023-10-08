class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         return self.process(word1, word2, 0, 0)
    
#     def process(self, word1, word2, i, j):
#         # operations needed to match word1[i:] and word2[j:]
#         if i == len(word1) and j == len(word2):
#             return 0
#         if i == len(word1):
#             return len(word2) - j
#         if j == len(word2):
#             return len(word1) - i
#         if word1[i] == word2[j]:
#             return self.process(word1, word2, i + 1, j + 1)
#         p1 = 1 + self.process(word1, word2, i + 1, j)
#         p2 = 1 + self.process(word1, word2, i, j + 1)
#         p3 = 1 + self.process(word1, word2, i + 1, j + 1)
#         return min(p1, p2, p3)
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        if not word1:
            return len2
        elif not word2:
            return len1
        dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        # dp[len1][len2] = 0
        for j in range(len2):
            dp[-1][j] = len2 - j
        for i in range(len1):
            dp[i][-1] = len1 - i
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    p1 = 1 + dp[i + 1][j]
                    p2 = 1 + dp[i][j + 1]
                    p3 = 1 + dp[i + 1][j + 1]
                    dp[i][j] = min(p1, p2, p3)
        return dp[0][0]
        