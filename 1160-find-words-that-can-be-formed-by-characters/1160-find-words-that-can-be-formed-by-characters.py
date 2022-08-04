class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res,counter=0,collections.Counter(chars)
        for w in words:
            wordCounter=collections.Counter(w)
            for c in wordCounter:
                if wordCounter[c]>counter[c]:
                    break
            else:
                res+=len(w)
        
        return res