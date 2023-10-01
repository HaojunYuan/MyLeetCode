class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # from left and right, take the longest
        res = 0
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                r += 1
            if l == r:
                res = max(res, l + r)
            elif r > l:
                l = r = 0
        l = r = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                r += 1
            elif s[i] == '(':
                l += 1
            
            if l == r:
                res = max(res, l + r)
            elif l > r:
                l = r = 0
                
        return res