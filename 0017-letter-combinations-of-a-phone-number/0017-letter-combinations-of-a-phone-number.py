class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return
        self.dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.res = []
        self.process(digits, 0, [])
        return self.res
    
    def process(self, digits, start, path):
        if start == len(digits):
            self.res.append(''.join(path))
            return
        letters = self.dic[digits[start]]
        for c in letters:
            path.append(c)
            self.process(digits, start + 1, path)
            path.pop()