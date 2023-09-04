class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res, buffer, in_comment_block = [], '', False
        for line in source:
            i = 0
            while i<len(line):
                char = line[i]
                if char == '/' and i + 1 < len(line) and line[i+1]=='/' and not in_comment_block:
                    i=len(line)
                elif char == '/' and i+1<len(line) and line[i+1]=='*' and not in_comment_block:
                    in_comment_block = True
                    i+=1
                elif char == '*' and i+1<len(line) and line[i+1]=='/' and in_comment_block:
                    in_comment_block = False
                    i+=1
                elif not in_comment_block:
                    buffer+=char
                i+=1
            if buffer and not in_comment_block:
                res.append(buffer)
                buffer = ''
        return res