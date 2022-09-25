class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res1=self.stack(s,[])
        res2=self.stack(t,[])
        return res1==res2
    
    def stack(self,s,stack):
        for char in s:
            if char!='#':
                stack.append(char)
            else:
                if not stack:
                    continue
                stack.pop()
        return stack