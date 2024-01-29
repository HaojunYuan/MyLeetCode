class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        if not word1:
            return l2
        if not word2:
            return l1
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for j in range(l2):
            dp[-1][j] = l2 - j
        for i in range(l1):
            dp[i][-1] = l1 - i
        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    p1 = dp[i][j + 1]
                    p2 = dp[i + 1][j]
                    p3 = dp[i + 1][j + 1]
                    dp[i][j] = 1 + min(p1, p2, p3)
        return dp[0][0]
#         return self.process(word1, word2, 0, 0)
    
#     def process(self, str1, str2, s1, s2):
#         # if we hit both end, return 0: nothing we can do
#         if s1 == len(str1) and s2 == len(str2):
#             return 0
#         # if we hit the end of one str, we can simply delete all extra chars
#         if s1 == len(str1):
#             return len(str2) - s2
#         if s2 == len(str2):
#             return len(str1) - s1
#         # in case two chars are the same
#         if str1[s1] == str2[s2]:
#             return self.process(str1, str2, s1 + 1, s2 + 1)
#         # 1. Move s1 to right, try to find a match
#         # 2. Move s2 to right
#         # 3. Take a step to replace a character, then move both pointers to right
#         p1 = 1 + self.process(str1, str2, s1 + 1, s2)
#         p2 = 1 + self.process(str1, str2, s1, s2 + 1)
#         p3 = 1 + self.process(str1, str2, s1 + 1, s2 + 1)
#         return min(p1, p2, p3)