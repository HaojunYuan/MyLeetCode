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
            return
        def helper(curr, i):
            if i == len(digits):
                res.append(curr)
                return
            for char in digitToChar[digits[i]]:
                curr += char
                helper(curr, i + 1)
                curr = curr[:-1]
        helper('', 0)
        return res