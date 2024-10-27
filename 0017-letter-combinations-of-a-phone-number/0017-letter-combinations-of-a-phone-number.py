class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
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
        self.process(0, digits, [])
        return self.res
    
    def process(self, start, digits, path):
        if start == len(digits):
            self.res.append(''.join(path))
            return
        for char in self.dic[digits[start]]:
            path.append(char)
            self.process(start + 1, digits, path)
            path.pop()