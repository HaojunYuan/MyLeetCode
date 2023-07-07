class Solution:
    def countSubstrings(self, s: str) -> int:
        # for each l and r, return the number of palindromes with l and r as center.
        # Every time l and r expand, the return value increase by 1 since we have 1 more palindrome with l and r as center
        res=0
        for i in range(len(s)):
            res1=self.expand(s,i,i)
            res2=self.expand(s,i,i+1)
            res=res+res1+res2
        return res
    
    def expand(self,s,l,r):
        res=0
        while l>=0 and r<len(s):
            if s[l]!=s[r]:
                break
            res+=1
            l-=1
            r+=1
        return res