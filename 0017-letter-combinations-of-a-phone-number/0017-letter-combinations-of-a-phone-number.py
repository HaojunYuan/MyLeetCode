class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return res
        
        def process(start, curr):
            if start == len(digits):
                res.append(curr)
                return
            for c in digitToChar[digits[start]]:
                curr += c
                process(start + 1, curr[:])
                curr = curr[:-1]
        process(0, '')
        return res