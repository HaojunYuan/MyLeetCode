class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c=Counter(p)
        l,r=0,0
        count=len(p)
        res=[]
        while r<len(s):
            if c[s[r]]>=1:
                count-=1
            c[s[r]]-=1
            r+=1
            if count==0:
                res.append(l)
            if r-l==len(p): #No matter if we found an index or not, we need to move the sliding window as soon as we reach the maximum size.
                if c[s[l]]>=0: #If s[l] is not in p, it would go negative. This indicates that s[l] is in p and therefore we need to increase count by 1, since after moving the left pointer 1 index to the right, we have 1 more character to match
                    count+=1
                c[s[l]]+=1
                l+=1
        return res
                
            