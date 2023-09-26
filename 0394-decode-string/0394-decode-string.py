class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ']':
                # start decoding from the stack
                string = ''
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)
                stack.append(num * string)
            else:
                stack.append(s[i])
        res = ''
        while stack:
            res = stack.pop() + res
        return res