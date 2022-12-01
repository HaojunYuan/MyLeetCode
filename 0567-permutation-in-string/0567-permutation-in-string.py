class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter=Counter(s1)
        l,r=0,0
        target=len(s1)
        while r<len(s2):
            if counter[s2[r]]>0: #s2[r] is in s1
                target-=1
            counter[s2[r]]-=1
            r+=1
            if target==0:
                return True
            if r-l==len(s1):
                if counter[s2[l]]>=0:
                    target+=1
                counter[s2[l]]+=1
                l+=1
        return False