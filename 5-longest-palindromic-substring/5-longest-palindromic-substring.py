class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        for i in range(len(s)):
            res1=self.expand(s,i,i)
            res2=self.expand(s,i,i+1)
            res=max(res1,res2,res,key=len)
        return res
    
    def expand(self,s:str, l, r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]
            