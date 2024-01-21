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
        # if s[i] > s[i + 1], proceed as usual
        # if s[i] < s[i + 1], we need to add s[i + 1] and minus s[i], and move i 2 indices forward
        i = 0
        res = 0
        while i < len(s):
            if i + 1 < len(s):
                if values[s[i]] >= values[s[i + 1]]:
                    res += values[s[i]]
                    i += 1
                else:
                    res = res + values[s[i + 1]] - values[s[i]]
                    i += 2
            else:
                res += values[s[i]]
                break
        return res
        
            