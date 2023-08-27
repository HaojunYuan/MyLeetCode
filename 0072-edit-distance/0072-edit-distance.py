class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         return self.process(word1, word2, 0, 0)
    
#     def process(self, s1, s2, i, j):
#         if i==len(s1) and j==len(s2):
#             return 0
#         # Delete all remaning characters in s2
#         if i==len(s1):
#             return len(s2)-j
#         # Delete all remaning characters in s1
#         if j==len(s2):
#             return len(s1)-i
#         if s1[i]==s2[j]:
#             return self.process(s1, s2, i+1, j+1)
#         else:
#             # Consider all 3 operations
#             # 1. Replace
#             p1 = 1 + self.process(s1, s2, i+1, j+1)
#             p2 = 1 + self.process(s1, s2, i+1, j)
#             p3 = 1 + self.process(s1, s2, i, j+1)
#             return min(p1, p2, p3)
    
    def minDistance(self, word1, word2):
        len1=len(word1)
        len2=len(word2)
        if not word1:
            return len2
        if not word2:
            return len1
        # Row: index of word1, col: index of word2
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        dp[len1][len2]=0
        # Initialize the table
        for j in range(len2+1):
            dp[len1][j]=len2-j
        for i in range(len1+1):
            dp[i][len2]=len1-i
        for i in range(len1-1, -1, -1):
            for j in range(len2-1, -1, -1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    p1 = 1+dp[i+1][j+1]
                    p2 = 1+dp[i+1][j]
                    p3 = 1+dp[i][j+1]
                    dp[i][j]=min(p1, p2, p3)
            
        return dp[0][0]
        
        