class Solution:
    def isValid(self, s: str) -> bool:
        dic={'(':')','[':']','{':'}'}
        stack=[]
        for char in s:
            if char in dic:
                stack+=char
            elif stack==[] or dic[stack[-1]]!=char:
                return False
            else:
                stack.pop()
        return stack==[]