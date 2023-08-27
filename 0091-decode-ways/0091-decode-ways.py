class Solution:
    def numDecodings(self, s: str) -> int:
        # try from left to right
        if not s:
            return 0
        dp=[0]*(len(s)+1)
        dp[len(s)]=1
        for i in range(len(s)-1, -1, -1):
            if s[i]=='0':
                dp[i]=0
                continue
            temp=0
            temp+=dp[i+1]
            if i+1<len(s) and int(s[i:i+2])<27:
                temp+=dp[i+2]
            dp[i]=temp
        return dp[0]
        
        
#         return self.process(s, 0)
    
#     def process(self, s, i):
#         # Base case
#         if i==len(s):
#             return 1
#         if s[i]=='0':
#             return 0
#         res=0
#         # s[i] is a single digit
#         res+=self.process(s, i+1)
#         # if s and s+1 is smaller than 26, add the possibility
#         if i+1<len(s) and int(s[i:i+2])<27:
#             res+=self.process(s, i+2)
#         return res
    
    