class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter=Counter(t)
        l,r=0,0
        start,end=0,0
        missing=len(t)
        minlen=math.inf
        while r<len(s):
            if counter[s[r]]>0:
                missing-=1
            counter[s[r]]-=1
            r+=1
            while missing==0:
                if r-l<minlen:
                    minlen=r-l
                    start,end=l,r
                if counter[s[l]]>=0:
                    missing+=1
                counter[s[l]]+=1
                l+=1
        return s[start:end]