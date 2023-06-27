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
        # like a subset with limited condition
        def backtrack(i, curr):
            if len(curr)==len(digits):
                res.append(curr)
                return
            # for each letter in number dictionary, we can choose to include it or not in the combination
            for l in digitToChar[digits[i]]:
                curr+=l
                backtrack(i+1, curr)
                curr=curr[:-1]
        if digits:
            backtrack(0,'')
        return res