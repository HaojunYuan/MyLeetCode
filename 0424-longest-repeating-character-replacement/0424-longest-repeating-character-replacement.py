class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic=defaultdict(int)
        l=0
        res=0
        maxcount=0
        for i in range(len(s)):
            dic[s[i]]+=1
            maxcount=max(maxcount,dic[s[i]])
            if i-l+1-maxcount>k:
                dic[s[l]]-=1
                l+=1
            res=max(i-l+1,res)
        return res
                