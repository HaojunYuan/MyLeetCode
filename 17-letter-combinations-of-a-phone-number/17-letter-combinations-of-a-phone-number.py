class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping=("0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz")
        res=[""]
        for i in digits:
            res=[p+q for p in res for q in mapping[int(i)]]
        return res if len(digits)>0 else []