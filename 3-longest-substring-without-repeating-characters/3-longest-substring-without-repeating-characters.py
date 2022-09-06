class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        res=0
        dic={}
        for i in range(len(s)):
            if s[i] in dic:
                left=max(left,dic[s[i]]+1)
            res=max(res,i-left+1)
            dic[s[i]]=i
        return res