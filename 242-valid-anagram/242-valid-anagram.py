class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counter=[0]*26
        for i in range(len(s)):
            counter[ord(s[i])-ord('a')]+=1
            counter[ord(t[i])-ord('a')]-=1
        for num in counter:
            if num!=0:
                return False
        return True
    #return Counter(s)==Counter(t)