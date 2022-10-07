class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        shortest=min(strs,key=len)
        for i,c in enumerate(shortest):
            for others in strs:
                if others[i]!=c:
                    return shortest[:i]
        return shortest