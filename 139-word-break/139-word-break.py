class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in wordDict:
                #d[i-len(w)] checks if there is a word ends before the start of                     curent word, and i-len(w) == -1 checks if the word starts from the                   beginnig of the string
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]