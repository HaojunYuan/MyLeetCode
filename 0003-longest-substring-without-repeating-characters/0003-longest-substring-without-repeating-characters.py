class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        dic={}
        for r in range(len(s)):
            if s[r] in dic:
                l=max(l,dic[s[r]]+1)
            dic[s[r]]=r
            res=max(res,r-l+1)
        return res