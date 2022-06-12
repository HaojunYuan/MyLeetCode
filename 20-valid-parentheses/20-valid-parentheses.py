class Solution:
    def isValid(self, s: str) -> bool:
        dic={'(':')','[':']','{':'}'}
        stack=[]
        for i in s:
            if i in dic:
                stack+=i
            elif stack and dic[stack[-1]]==i:
                stack.pop()
            else:
                return False
        return stack==[]