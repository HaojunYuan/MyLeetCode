class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        pre=0
        res=values[s[0]]
        
        for i in range(1,len(s)):
            if values[s[pre]]<values[s[i]]:
                res=res-values[s[pre]]-values[s[pre]]
                res+=values[s[i]]
            else:
                res+=values[s[i]]
            pre=i
        
        return res
            