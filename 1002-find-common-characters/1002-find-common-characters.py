class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res=list(words[0])
        for word in words:
            newRes=[]
            for char in word:
                if char in res:
                    newRes.append(char)
                    res.remove(char)
            res=newRes
        return res