class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        MAPPING = ('0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')
        res = ['']
        for d in digits:
            res=[pre + cur for pre in res for cur in MAPPING[int(d)]]
        return res if len(digits) > 0 else []