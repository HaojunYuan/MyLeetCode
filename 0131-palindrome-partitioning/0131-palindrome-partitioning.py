class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.process(s, 0, [], res)
        return res
    
    def process(self, s, start, curr, res):
        if start == len(s):
            res.append(curr[:])
            return
        for i in range(start, len(s)):
            if self.isPalindrome(s, start, i):
                curr.append(s[start:i + 1])
                self.process(s, i + 1, curr, res)
                curr.pop()
        
    def isPalindrome(self, s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True