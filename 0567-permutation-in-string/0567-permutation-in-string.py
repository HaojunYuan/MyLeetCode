class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c=Counter(s1)
        l,r=0,0
        target=len(s1)
        while r<len(s2):
            if c[s2[r]]>0:
                target-=1
            c[s2[r]]-=1
            r+=1
            if target==0:
                return True
            if r-l==len(s1):
                if c[s2[l]]>=0:
                    target+=1
                c[s2[l]]+=1
                l+=1
        return False