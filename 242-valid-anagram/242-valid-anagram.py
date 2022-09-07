class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #use defaultdict
        if len(s)!=len(t):
            return False
        counter=defaultdict(int)
        for i in range(len(s)):
            counter[s[i]]+=1
            counter[t[i]]-=1
        for key,value in counter.items():
            if value!=0:
                return False
        return True
            