class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter=Counter(p)
        l,r=0,0
        res=[]
        count=len(p)
        while r<len(s):
            if counter[s[r]]>0:
                count-=1
            counter[s[r]]-=1
            r+=1
            if count==0:
                res.append(l)
            if r-l==len(p):
                if counter[s[l]]>=0:
                    count+=1
                counter[s[l]]+=1
                l+=1
        return res