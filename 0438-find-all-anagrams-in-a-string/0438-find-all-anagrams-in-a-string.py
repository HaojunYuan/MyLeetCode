class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter=Counter(p)
        l,r=0,0
        res=[]
        target=len(p)
        while r<len(s):
            if counter[s[r]]>0:
                target-=1
            counter[s[r]]-=1
            r+=1
            if target==0:
                res.append(l)
            if r-l==len(p):
                if counter[s[l]]>=0:
                    target+=1
                counter[s[l]]+=1
                l+=1
        return res