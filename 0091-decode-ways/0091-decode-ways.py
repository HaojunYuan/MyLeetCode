class Solution:
    def numDecodings(self, s: str) -> int:
        # DP
        if not s:
            return 0
        dp = [0]*(len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s)-1, -1, -1):
            if s[i] != '0':
                dp[i] += dp[i+1]
                if i+1<len(s) and int(s[i:i+2]) < 27:
                    dp[i] += dp[i+2]
        return dp[0]
        
#         return self.process(s, 0)
    
#     # Return the number of decode ways starting from index i
#     def process(self, s, i):
#         if i==len(s):
#             return 1
#         if s[i]=='0':
#             return 0
#         res = 0
#         res += self.process(s, i+1)
#         if i+1<len(s) and int(s[i:i+2])<27:
#             res += self.process(s, i+2)
#         return res