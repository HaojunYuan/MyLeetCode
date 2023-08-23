class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        dp=[0]*(len(s)+1)
        dp[-1]=1
        for i in range(len(s)-1,-1,-1):
            if s[i]!='0':
                dp[i]=dp[i+1]
                if i+1<len(s) and int(s[i:i+2])<27:
                    dp[i]+=dp[i+2]
        return dp[0]